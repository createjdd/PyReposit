#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BOSS直聘爬虫脚本
抓取职位详情：薪资、职位描述、公司介绍、工商信息、工作地址
"""

import time # 时间模块
import random # 随机模块
import re # 正则表达式模块
import pandas as pd # 数据处理模块
from selenium import webdriver # 浏览器驱动模块
from selenium.webdriver.common.by import By # 元素选择器模块
from selenium.webdriver.support.ui import WebDriverWait # 等待模块
from selenium.webdriver.support import expected_conditions as EC # 预期条件模块
from selenium.webdriver.chrome.service import Service # 浏览器服务模块
from selenium.webdriver.chrome.options import Options # 浏览器选项模块
from selenium.common.exceptions import TimeoutException, NoSuchElementException # 异常模块
import logging

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class BossSpider:
    def __init__(self):
        """初始化爬虫"""
        self.driver = None # 浏览器驱动
        self.data = [] # 数据列表
        self.target_count = 10 # 目标职位数量
        self.base_url = "https://www.zhipin.com" # 基础URL
        
    def init_driver(self):
        """初始化浏览器驱动"""
        chrome_options = Options()
        
        # 反爬虫设置：模拟真实浏览器
        chrome_options.add_argument('--disable-blink-features=AutomationControlled') # 禁用自动化控制
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"]) # 禁用自动化控制
        chrome_options.add_experimental_option('useAutomationExtension', False) # 禁用自动化扩展
        
        # 设置用户代理
        chrome_options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36') # 设置用户代理
        
        # 可选：无头模式（注释掉以显示浏览器窗口，方便调试）
        # chrome_options.add_argument('--headless')
        
        # 其他设置
        chrome_options.add_argument('--no-sandbox') # 禁用沙盒
        chrome_options.add_argument('--disable-dev-shm-usage') # 禁用开发共享内存使用
        chrome_options.add_argument('--window-size=1920,1080') # 设置窗口大小
        
        try:
            self.driver = webdriver.Chrome(options=chrome_options) # 创建浏览器驱动
            # 执行反检测脚本
            self.driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
                'source': '''
                    Object.defineProperty(navigator, 'webdriver', {
                        get: () => undefined
                    })
                '''
            })
            logger.info("浏览器驱动初始化成功")
        except Exception as e:
            logger.error(f"浏览器驱动初始化失败: {e}")
            raise
    
    def random_delay(self, min_sec=1, max_sec=3):
        """随机延迟，模拟人类操作"""
        delay = random.uniform(min_sec, max_sec)
        time.sleep(delay)
        return delay
    
    def human_scroll(self):
        """模拟人类滚动行为"""
        try:
            # 随机滚动距离
            scroll_pause = random.uniform(0.5, 1.5)
            scroll_amount = random.randint(300, 800)
            
            self.driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
            time.sleep(scroll_pause)
            
            # 偶尔向上滚动一点，模拟真实浏览
            if random.random() < 0.3:
                self.driver.execute_script(f"window.scrollBy(0, -{random.randint(50, 200)});")
                time.sleep(random.uniform(0.3, 0.8))
        except Exception as e:
            logger.debug(f"human_scroll出错: {e}")
    
    def scroll_to_load_more(self, current_count):
        """滚动页面以加载更多职位"""
        last_count = current_count
        no_change_count = 0
        max_scroll_attempts = 20  # 最多滚动20次
        
        # 等待页面初始加载
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "body"))
            )
            self.random_delay(2, 3)  # 额外等待页面渲染
        except TimeoutException:
            logger.warning("页面加载超时，继续尝试滚动")
        
        scroll_attempts = 0
        while len(self.data) < self.target_count and scroll_attempts < max_scroll_attempts:
            scroll_attempts += 1
            
            # 安全地滚动到底部
            try:
                # 使用更安全的滚动方式
                scroll_script = """
                var body = document.body || document.documentElement;
                if (body) {
                    window.scrollTo(0, Math.max(
                        body.scrollHeight,
                        document.documentElement.scrollHeight,
                        body.offsetHeight,
                        document.documentElement.offsetHeight,
                        body.clientHeight,
                        document.documentElement.clientHeight
                    ));
                }
                """
                self.driver.execute_script(scroll_script)
                self.random_delay(1, 2)
            except Exception as e:
                logger.warning(f"滚动时出错: {e}")
                # 尝试简单的滚动
                try:
                    self.driver.execute_script("window.scrollBy(0, 1000);")
                    self.random_delay(1, 2)
                except:
                    pass
            
            # 尝试查找职位列表
            try:
                items = self.driver.find_elements(By.CSS_SELECTOR, ".job-card-wrapper, .job-card-item, [class*='item'], a[href*='job_detail']")
                current_count = len(items)
                
                if current_count == last_count:
                    no_change_count += 1
                    if no_change_count >= 3:
                        logger.info("已加载所有职位，停止滚动")
                        break
                else:
                    no_change_count = 0
                    last_count = current_count
                    logger.info(f"当前已加载 {current_count} 个职位")
                
            except Exception as e:
                logger.warning(f"查找职位列表时出错: {e}")
            
            # 如果已经抓取足够的数据，停止滚动
            if len(self.data) >= self.target_count:
                break
            
            # 随机滚动行为
            try:
                self.human_scroll()
            except Exception as e:
                logger.debug(f"随机滚动出错: {e}")
        
        if scroll_attempts >= max_scroll_attempts:
            logger.info(f"达到最大滚动次数 ({max_scroll_attempts})，停止滚动")
    
    def extract_job_detail_from_current_page(self):
        """从当前页面提取职位详情（用于点击方式）"""
        try:
            # 等待页面加载
            self.random_delay(1, 2)
            
            # 等待关键元素加载
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".job-sec, .job-detail, [class*='detail'], body"))
                )
            except TimeoutException:
                logger.warning("页面加载超时")
                return None
            
            return self._extract_job_data()
        except Exception as e:
            logger.error(f"从当前页面提取数据时出错: {e}")
            return None
    
    def extract_job_detail(self, detail_url):
        """提取职位详情页数据（使用新标签页方式）"""
        original_window = self.driver.current_window_handle
        
        try:
            # 打开新标签页
            self.driver.execute_script(f"window.open('{detail_url}', '_blank');")
            self.driver.switch_to.window(self.driver.window_handles[-1])
            
            # 等待页面加载
            self.random_delay(2, 4)
            
            # 等待关键元素加载
            try:
                WebDriverWait(self.driver, 15).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "body"))
                )
                # 额外等待一下，确保动态内容加载完成
                self.random_delay(1, 2)
            except TimeoutException:
                logger.warning(f"页面加载超时: {detail_url}")
                self.driver.close()
                self.driver.switch_to.window(original_window)
                return None
            
            # 提取数据
            job_data = self._extract_job_data()
            
            # 关闭详情页标签
            self.driver.close()
            self.driver.switch_to.window(original_window)
            
            # 等待一下再继续
            self.random_delay(0.5, 1)
            return job_data
            
        except Exception as e:
            logger.error(f"提取职位详情时出错: {e}")
            import traceback
            logger.debug(traceback.format_exc())
            try:
                # 确保关闭新标签页并切换回原窗口
                if len(self.driver.window_handles) > 1:
                    self.driver.close()
                self.driver.switch_to.window(original_window)
            except:
                pass
            return None
    
    def _extract_job_data(self):
        """提取职位数据的核心逻辑"""
        job_data = {
            '薪资': '',
            '职位描述': '',
            '公司介绍': '',
            '工商信息': '',
            '工作地址': ''
        }
        
        # 提取薪资 - 通常在页面顶部，优先提取
        try:
            salary_selectors = [
                ".salary",  # 最常见的薪资选择器
                "[class*='salary']",  # 包含salary的类
                ".job-primary .salary",  # 主要信息中的薪资
                ".job-header .salary",  # 职位头部中的薪资
                ".job-info .salary",  # 职位信息中的薪资
                "[class*='job-primary'] [class*='salary']",  # 嵌套结构
                ".job-detail-header .salary",  # 详情头部中的薪资
                "span[class*='salary']",  # span标签中的薪资
                "div[class*='salary']"  # div标签中的薪资
            ]
            
            for selector in salary_selectors:
                try:
                    elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
                    for element in elements:
                        text = element.text.strip()
                        # 薪资通常包含"K"、"万"、"元"等关键词，或者包含数字和"-"
                        if text and (any(keyword in text for keyword in ['K', 'k', '万', '元', '-']) or 
                                   any(char.isdigit() for char in text)):
                            job_data['薪资'] = text
                            logger.debug(f"使用选择器 '{selector}' 提取到薪资: {text}")
                            break
                    if job_data['薪资']:
                        break
                except Exception as e:
                    logger.debug(f"选择器 '{selector}' 失败: {e}")
                    continue
            
            # 如果还没找到，尝试在职位头部区域查找包含薪资格式的文本
            if not job_data['薪资']:
                try:
                    # 查找职位头部区域
                    header_selectors = [
                        ".job-primary",
                        ".job-header",
                        ".job-info",
                        "[class*='job-primary']",
                        "[class*='job-header']"
                    ]
                    for header_selector in header_selectors:
                        try:
                            headers = self.driver.find_elements(By.CSS_SELECTOR, header_selector)
                            for header in headers:
                                header_text = header.text
                                # 查找包含薪资格式的文本（如：15K-30K、10-20万等）
                                salary_patterns = [
                                    r'\d+[Kk]-\d+[Kk]',  # 15K-30K
                                    r'\d+-\d+[万]',  # 10-20万
                                    r'\d+-\d+[元]',  # 5000-10000元
                                    r'\d+[Kk]',  # 15K
                                    r'\d+[万]',  # 10万
                                ]
                                for pattern in salary_patterns:
                                    matches = re.findall(pattern, header_text)
                                    if matches:
                                        job_data['薪资'] = matches[0]
                                        logger.debug(f"通过正则表达式找到薪资: {matches[0]}")
                                        break
                                if job_data['薪资']:
                                    break
                            if job_data['薪资']:
                                break
                        except Exception as e:
                            logger.debug(f"查找头部区域失败: {e}")
                            continue
                except Exception as e:
                    logger.debug(f"通过头部区域查找薪资失败: {e}")
                    
        except Exception as e:
            logger.warning(f"提取薪资失败: {e}")
        
        # 提取职位描述 - 尝试多种选择器（BOSS直聘常见结构）
        try:
            job_desc_selectors = [
                ".job-sec-text",  # 最常见的职位描述选择器
                ".job-detail-section .text",  # 详情区域的文本
                ".job-sec .text",  # 职位区域文本
                "[class*='job-sec-text']",  # 包含job-sec-text的类
                "[class*='job-desc']",  # 包含job-desc的类
                ".job-detail-text",  # 详情文本
                ".job-sec-text-box",  # 文本盒子
                ".job-detail .text",  # 详情页文本
                ".job-sec-box .text",  # 职位区域盒子文本
                "div[class*='job-sec'] div[class*='text']",  # 嵌套结构
                ".job-sec-wrapper .text"  # 包装器内的文本
            ]
            
            for selector in job_desc_selectors:
                try:
                    elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
                    for element in elements:
                        text = element.text.strip()
                        # 职位描述通常比较长，至少50个字符
                        if text and len(text) > 50:
                            job_data['职位描述'] = text
                            logger.debug(f"使用选择器 '{selector}' 提取到职位描述 ({len(text)} 字符)")
                            break
                    if job_data['职位描述']:
                        break
                except Exception as e:
                    logger.debug(f"选择器 '{selector}' 失败: {e}")
                    continue
                    
            # 如果还没找到，尝试查找所有包含"职位描述"或"岗位职责"的section
            if not job_data['职位描述']:
                try:
                    # 查找所有job-sec开头的section
                    sections = self.driver.find_elements(By.CSS_SELECTOR, "[class*='job-sec']")
                    for section in sections:
                        section_text = section.text.strip()
                        # 检查是否包含职位描述相关关键词
                        if section_text and len(section_text) > 50:
                            # 检查section标题
                            try:
                                title = section.find_element(By.CSS_SELECTOR, "h3, .title, [class*='title']")
                                title_text = title.text.strip()
                                if any(keyword in title_text for keyword in ['职位描述', '岗位职责', '工作内容', '职位详情']):
                                    job_data['职位描述'] = section_text
                                    logger.debug(f"通过section标题找到职位描述")
                                    break
                            except:
                                # 如果没有标题，但内容足够长，也可能是职位描述
                                if len(section_text) > 100:
                                    job_data['职位描述'] = section_text
                                    logger.debug(f"通过长文本找到职位描述")
                                    break
                except Exception as e:
                    logger.debug(f"通过section查找失败: {e}")
                    
        except Exception as e:
            logger.warning(f"提取职位描述失败: {e}")
        
        # 提取公司介绍
        try:
            company_selectors = [
                ".company-intro",  # 公司介绍
                "[class*='company-intro']",  # 包含company-intro的类
                ".company-desc",  # 公司描述
                ".job-sec-company",  # 公司区域
                ".company-info-text",  # 公司信息文本
                "[class*='company-desc']",  # 包含company-desc的类
                ".company-sec-text",  # 公司区域文本
                ".company-sec .text",  # 公司区域内的文本
                "div[class*='company'] div[class*='text']"  # 嵌套结构
            ]
            for selector in company_selectors:
                try:
                    elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
                    for element in elements:
                        text = element.text.strip()
                        if text and len(text) > 10:  # 公司介绍至少10个字符
                            job_data['公司介绍'] = text
                            logger.debug(f"使用选择器 '{selector}' 提取到公司介绍")
                            break
                    if job_data['公司介绍']:
                        break
                except Exception as e:
                    logger.debug(f"选择器 '{selector}' 失败: {e}")
                    continue
        except Exception as e:
            logger.warning(f"提取公司介绍失败: {e}")
        
        # 提取工商信息
        try:
            business_selectors = [
                ".business-info",  # 工商信息
                "[class*='business-info']",  # 包含business-info的类
                "[class*='business']",  # 包含business的类
                ".company-info",  # 公司信息
                "[class*='company-info']",  # 包含company-info的类
                ".business-license",  # 营业执照
                "[class*='business-license']",  # 包含business-license的类
                ".company-license",  # 公司执照
                "[class*='license']",  # 包含license的类
                ".company-detail-info",  # 公司详情信息
                "div[class*='business']",  # 工商相关div
                "div[class*='license']"  # 执照相关div
            ]
            
            for selector in business_selectors:
                try:
                    elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
                    for element in elements:
                        text = element.text.strip()
                        if text:
                            # 工商信息通常包含：公司名称、法人、注册资本等关键词
                            if any(keyword in text for keyword in ['法人', '注册资本', '成立', '统一社会信用代码', '注册号']):
                                job_data['工商信息'] = text
                                logger.debug(f"使用选择器 '{selector}' 提取到工商信息")
                                break
                    if job_data['工商信息']:
                        break
                except Exception as e:
                    logger.debug(f"选择器 '{selector}' 失败: {e}")
                    continue
            
            # 如果还没找到，尝试查找包含"工商"关键词的section
            if not job_data['工商信息']:
                try:
                    sections = self.driver.find_elements(By.CSS_SELECTOR, "[class*='sec'], [class*='section']")
                    for section in sections:
                        section_text = section.text.strip()
                        if section_text and any(keyword in section_text for keyword in ['法人', '注册资本', '成立', '统一社会信用代码']):
                            job_data['工商信息'] = section_text
                            logger.debug(f"通过关键词找到工商信息")
                            break
                except Exception as e:
                    logger.debug(f"通过关键词查找失败: {e}")
                    
        except Exception as e:
            logger.warning(f"提取工商信息失败: {e}")
        
        # 提取工作地址
        try:
            address_selectors = [
                ".job-location",  # 工作地点
                "[class*='location']",  # 包含location的类
                ".job-address",  # 工作地址
                "[class*='address']",  # 包含address的类
                ".location-address",  # 地点地址
                ".job-location-address",  # 工作地点地址
                "[class*='job-location']",  # 包含job-location的类
                ".location-text",  # 地点文本
                "[class*='location-text']",  # 包含location-text的类
                ".job-primary .location",  # 主要信息中的地点
                "[data-v-] .location"  # Vue组件中的地点
            ]
            for selector in address_selectors:
                try:
                    elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
                    for element in elements:
                        text = element.text.strip()
                        if text:
                            job_data['工作地址'] = text
                            logger.debug(f"使用选择器 '{selector}' 提取到工作地址")
                            break
                    if job_data['工作地址']:
                        break
                except Exception as e:
                    logger.debug(f"选择器 '{selector}' 失败: {e}")
                    continue
        except Exception as e:
            logger.warning(f"提取工作地址失败: {e}")
        
        return job_data
    
    def get_job_list_items(self):
        """获取职位列表页的所有职位项元素"""
        items = []
        
        # 尝试多种选择器来查找职位项（优先使用class="item"）
        selectors = [
            ".item",  # 用户指定的选择器
            "[class*='item']",
            ".job-card-wrapper",
            ".job-card-item",
            "[class*='job-card']",
            ".job-list-box > *",
            ".job-primary"
        ]
        
        for selector in selectors:
            try:
                found_items = self.driver.find_elements(By.CSS_SELECTOR, selector)
                if found_items:
                    logger.info(f"使用选择器 '{selector}' 找到 {len(found_items)} 个职位项")
                    # 过滤出有效的职位项（包含job_detail链接的）
                    for item in found_items:
                        try:
                            # 检查是否包含职位详情链接
                            link = item.find_element(By.CSS_SELECTOR, "a[href*='job_detail']")
                            if link:
                                items.append(item)
                        except:
                            try:
                                # 或者元素本身是可点击的
                                if item.get_attribute("href") and "job_detail" in item.get_attribute("href"):
                                    items.append(item)
                            except:
                                pass
                    if items:
                        break
            except Exception as e:
                logger.debug(f"选择器 '{selector}' 未找到元素: {e}")
                continue
        
        logger.info(f"共找到 {len(items)} 个有效职位项")
        return items
    
    def get_job_list_urls(self):
        """获取职位列表页的所有职位链接"""
        urls = []
        seen_urls = set()  # 用于去重
        
        # 尝试多种选择器来查找职位链接（优先使用用户指定的.item选择器）
        selectors = [
            ".item a[href*='job_detail']",  # 用户指定的.item选择器
            "a[href*='job_detail']",  # 直接找所有包含job_detail的链接
            ".job-card-wrapper a[href*='job_detail']",
            ".job-card-item a[href*='job_detail']",
            "[class*='job-card'] a[href*='job_detail']",
            "[class*='item'] a[href*='job_detail']",
            ".job-list-box a[href*='job_detail']",
            ".job-primary a[href*='job_detail']",
            "a[ka*='job'][href*='job_detail']"
        ]
        
        # 先尝试直接找链接
        for selector in selectors:
            try:
                links = self.driver.find_elements(By.CSS_SELECTOR, selector)
                if links:
                    logger.info(f"使用选择器 '{selector}' 找到 {len(links)} 个链接")
                    for link in links:
                        try:
                            href = link.get_attribute("href")
                            if href and "job_detail" in href:
                                # 清理URL，移除可能的参数，但保留基本路径
                                if '?' in href:
                                    # 保留一些有用的参数，移除追踪参数
                                    url_parts = href.split('?')
                                    base_url = url_parts[0]
                                    # 只保留必要的参数
                                    params = url_parts[1] if len(url_parts) > 1 else ''
                                    # 移除追踪参数
                                    if 'ka=' in params or 'lid=' in params:
                                        clean_url = base_url
                                    else:
                                        clean_url = href
                                else:
                                    clean_url = href
                                
                                # 去重
                                if clean_url not in seen_urls:
                                    seen_urls.add(clean_url)
                                    urls.append(clean_url)
                        except Exception as e:
                            logger.debug(f"处理链接时出错: {e}")
                            pass
                    
                    # 如果找到足够的链接，可以继续尝试其他选择器以获取更多
                    if len(urls) >= self.target_count:
                        logger.info(f"已找到足够的链接 ({len(urls)} 个)")
                        break
            except Exception as e:
                logger.debug(f"选择器 '{selector}' 未找到元素: {e}")
                continue
        
        # 如果直接找链接不够，尝试通过容器元素找
        if len(urls) < self.target_count:
            container_selectors = [
                ".item",  # 用户指定的选择器
                ".job-card-wrapper",
                ".job-card-item",
                "[class*='job-card']",
                "[class*='item']"
            ]
            
            for selector in container_selectors:
                try:
                    items = self.driver.find_elements(By.CSS_SELECTOR, selector)
                    if items:
                        logger.info(f"使用容器选择器 '{selector}' 找到 {len(items)} 个职位项")
                        for item in items:
                            try:
                                # 在容器内找链接
                                link = item.find_element(By.CSS_SELECTOR, "a[href*='job_detail']")
                                href = link.get_attribute("href")
                                if href and "job_detail" in href:
                                    clean_url = href.split('?')[0] if '?' in href else href
                                    if clean_url not in seen_urls:
                                        seen_urls.add(clean_url)
                                        urls.append(clean_url)
                            except:
                                try:
                                    # 或者元素本身是链接
                                    href = item.get_attribute("href")
                                    if href and "job_detail" in href:
                                        clean_url = href.split('?')[0] if '?' in href else href
                                        if clean_url not in seen_urls:
                                            seen_urls.add(clean_url)
                                            urls.append(clean_url)
                                except:
                                    pass
                        
                        if len(urls) >= self.target_count:
                            break
                except Exception as e:
                    logger.debug(f"容器选择器 '{selector}' 未找到元素: {e}")
                    continue
        
        logger.info(f"共收集到 {len(urls)} 个唯一职位链接")
        return urls
    
    def crawl(self, start_url):
        """主爬取函数"""
        try:
            self.init_driver()
            
            # 访问起始页面
            logger.info(f"正在访问: {start_url}")
            self.driver.get(start_url)
            self.random_delay(3, 5)
            
            # 等待页面加载
            try:
                WebDriverWait(self.driver, 15).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "body"))
                )
            except TimeoutException:
                logger.error("页面加载超时")
                return
            
            # 滚动加载更多职位
            logger.info("开始滚动加载更多职位...")
            self.scroll_to_load_more(0)
            
            # 获取所有职位URL（使用URL方式，避免stale element问题）
            logger.info("正在收集职位URL...")
            job_urls = self.get_job_list_urls()
            
            if not job_urls:
                logger.error("未找到任何职位URL")
                return
            
            # 限制抓取数量
            job_urls = job_urls[:self.target_count]
            total_count = len(job_urls)
            logger.info(f"共找到 {total_count} 个职位URL，开始抓取...")
            
            # 遍历每个职位
            for idx, job_url in enumerate(job_urls, 1):
                if len(self.data) >= self.target_count:
                    break
                
                try:
                    logger.info(f"[{idx}/{total_count}] 正在抓取: {job_url}")
                    
                    # 确保URL完整
                    if not job_url.startswith("http"):
                        job_url = self.base_url + job_url
                    
                    # 使用URL方式访问详情页
                    job_data = self.extract_job_detail(job_url)
                    
                    if job_data:
                        job_data['职位链接'] = job_url
                        self.data.append(job_data)
                        logger.info(f"✓ 成功抓取第 {len(self.data)} 个职位")
                        # 打印提取到的数据摘要
                        logger.info(f"  - 薪资: {job_data['薪资'] if job_data['薪资'] else '无'}")
                        logger.info(f"  - 职位描述: {'有' if job_data['职位描述'] else '无'} ({len(job_data['职位描述'])} 字符)")
                        logger.info(f"  - 公司介绍: {'有' if job_data['公司介绍'] else '无'} ({len(job_data['公司介绍'])} 字符)")
                        logger.info(f"  - 工商信息: {'有' if job_data['工商信息'] else '无'} ({len(job_data['工商信息'])} 字符)")
                        logger.info(f"  - 工作地址: {'有' if job_data['工作地址'] else '无'} ({len(job_data['工作地址'])} 字符)")
                    else:
                        logger.warning(f"✗ 抓取失败: {job_url}")
                    
                    # 随机延迟，模拟人类行为
                    if idx < total_count:
                        delay = self.random_delay(2, 5)
                        logger.info(f"等待 {delay:.2f} 秒后继续...\n")
                
                except Exception as e:
                    logger.error(f"处理第 {idx} 个职位时出错: {e}")
                    import traceback
                    logger.debug(traceback.format_exc())
                    continue
            
            logger.info(f"共抓取 {len(self.data)} 个职位数据")
            
        except Exception as e:
            logger.error(f"爬取过程中出错: {e}")
        finally:
            if self.driver:
                self.driver.quit()
                logger.info("浏览器已关闭")
    
    def save_to_excel(self, filename="boss_jobs.xlsx"):
        """保存数据到Excel文件"""
        if not self.data:
            logger.warning("没有数据可保存")
            return
        
        df = pd.DataFrame(self.data)
        df.to_excel(filename, index=False, engine='openpyxl')
        logger.info(f"数据已保存到 {filename}")
        logger.info(f"共 {len(df)} 条记录")
    
    def save_to_csv(self, filename="boss_jobs.csv"):
        """保存数据到CSV文件"""
        if not self.data:
            logger.warning("没有数据可保存")
            return
        
        df = pd.DataFrame(self.data)
        df.to_csv(filename, index=False, encoding='utf-8-sig')
        logger.info(f"数据已保存到 {filename}")
        logger.info(f"共 {len(df)} 条记录")


def main():
    """主函数"""
    start_url = "https://www.zhipin.com/web/geek/jobs?query=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91&city=101010100&position=101401"
    
    spider = BossSpider() # 创建爬虫对象
    spider.crawl(start_url) # 爬取数据
    
    # 保存数据
    if spider.data:
        spider.save_to_excel("boss_jobs.xlsx")
        spider.save_to_csv("boss_jobs.csv")
    else:
        logger.warning("未抓取到任何数据")


if __name__ == "__main__":
    main()


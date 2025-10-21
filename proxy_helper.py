"""
Free Proxy Helper for FIREx Bot
Gets free working proxies for bypassing 403 errors
"""

import requests
import logging
import random
import time

logger = logging.getLogger(__name__)

class ProxyManager:
    def __init__(self):
        self.working_proxies = []
        self.proxy_sources = [
            'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all',
        ]
    
    def fetch_free_proxies(self):
        """Fetch free proxies from ProxyScrape API"""
        try:
            logger.info("🔍 Fetching free proxies...")
            response = requests.get(self.proxy_sources[0], timeout=10)
            
            if response.status_code == 200:
                proxies = response.text.split('\n')
                proxy_list = [p.strip() for p in proxies if p.strip() and ':' in p]
                logger.info(f"✅ Found {len(proxy_list)} proxies")
                return proxy_list[:50]  # Take first 50
            else:
                logger.error(f"Failed to fetch proxies: {response.status_code}")
                return []
                
        except Exception as e:
            logger.error(f"Error fetching proxies: {e}")
            return []
    
    def test_proxy(self, proxy, test_url='http://httpbin.org/ip'):
        """Test if a proxy works"""
        try:
            proxies = {
                'http': f'http://{proxy}',
                'https': f'http://{proxy}'
            }
            
            response = requests.get(
                test_url,
                proxies=proxies,
                timeout=5
            )
            
            if response.status_code == 200:
                return True
        except:
            pass
        return False
    
    def get_working_proxies(self, max_test=20):
        """Get list of working proxies"""
        if self.working_proxies:
            return self.working_proxies
        
        logger.info("🧪 Testing proxies...")
        proxy_list = self.fetch_free_proxies()
        
        for proxy in proxy_list[:max_test]:
            if self.test_proxy(proxy):
                self.working_proxies.append(proxy)
                logger.info(f"✅ Working proxy: {proxy}")
            
            if len(self.working_proxies) >= 5:
                break
        
        logger.info(f"✅ Found {len(self.working_proxies)} working proxies")
        return self.working_proxies
    
    def get_random_proxy(self):
        """Get a random working proxy"""
        if not self.working_proxies:
            self.get_working_proxies()
        
        if self.working_proxies:
            proxy = random.choice(self.working_proxies)
            return {
                'http': f'http://{proxy}',
                'https': f'http://{proxy}'
            }
        return None
    
    def make_request_with_proxy(self, url, **kwargs):
        """Make request with automatic proxy rotation"""
        max_retries = 3
        
        for attempt in range(max_retries):
            proxy_dict = self.get_random_proxy()
            
            if not proxy_dict:
                logger.warning("⚠️ No working proxies available!")
                # Try without proxy
                try:
                    return requests.get(url, **kwargs)
                except:
                    return None
            
            try:
                logger.info(f"🔄 Attempt {attempt + 1} with proxy...")
                response = requests.get(url, proxies=proxy_dict, **kwargs)
                
                if response.status_code == 200:
                    logger.info("✅ Request successful with proxy!")
                    return response
                else:
                    logger.warning(f"⚠️ Got {response.status_code}, trying next proxy...")
                    
            except Exception as e:
                logger.error(f"❌ Proxy failed: {e}")
                continue
        
        return None


# Singleton instance
_proxy_manager = None

def get_proxy_manager():
    global _proxy_manager
    if _proxy_manager is None:
        _proxy_manager = ProxyManager()
    return _proxy_manager

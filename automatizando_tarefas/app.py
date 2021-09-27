from selenium import webdriver
from time import sleep


class ChromeAuto:
    def __init__(self):
        self.driver_path = 'chromedriver.exe'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('user-data=Perfil')
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )

    def clica_sign_in(self):
        try:
            try:
                btn_sign_in = self.chrome.find_element_by_css_selector(
                    'body > div.position-relative.js-header-wrapper > header > div > div.d-flex.flex-justify-between.flex-items-center > div.d-flex.flex-items-center > button > svg')
                btn_sign_in.click()
                btn_sign_in2 = self.chrome.find_element_by_link_text('Sign in')
                btn_sign_in2.click()
            except Exception as e:
                pass
            try:
                btn_sign_in = self.chrome.find_element_by_link_text('Sign in')
            except Exception as e:
                pass
        except Exception as e:
            print(f'Erro ao clicar em Sign in: {e}')

    def acessa(self, site):
        self.chrome.get(site)

    def sair(self):
        self.chrome.quit()

    def clica_perfil(self):
        try:
            perfil = self.chrome.find_element_by_css_selector('body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > summary')
            perfil.click()
        except Exception as e:
            print(f'Erro ao clilcar no perfil: {e}')

    def faz_logout(self):
        try:
            try:
                perfil = self.chrome.find_element_by_css_selector('body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > details-menu > form > button')
                perfil.click()
            except:
                pass
            try:
                perfil2 = self.chrome.find_element_by_link_text('Sign out')
                perfil2.click()
            except:
                pass
        except Exception as e:
            print(f'Erro ao fazer o logout: {e}')

    def faz_login(self):
        try:
            input_login = self.chrome.find_element_by_id('login_field')
            input_password = self.chrome.find_element_by_id('password')
            btn_login = self.chrome.find_element_by_name('commit')

            input_login.send_keys('Cica013')
            input_password.send_keys('**********')
            sleep(3)
            btn_login.click()

        except Exception as e:
            print(f'Erro ao fazer o login: {e}')


if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.acessa('https://github.com')


    chrome.clica_sign_in()
    chrome.faz_login()
    sleep(5)

    chrome.clica_perfil()
    chrome.faz_logout()

    sleep(5)
    chrome.sair()

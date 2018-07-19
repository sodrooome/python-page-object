class HomePage(object):
    """Represent home page web element locators."""

    logo: str = "//img[@alt='Mercury Tours']"
    sing_on: str = "//a[contains(text(), 'SIGN-ON')]"
    register: str = "//a[contains(text(), 'REGISTER')]"
    support: str = "//a[contains(text(), 'SUPPORT')]"
    contact: str = "//a[contains(text(), 'CONTACT')]"


class RegistrationPage(object):
    """Represent registration page web element locators."""

    regis_txt: str = "//*[contains(text(), 'basic information')]"
    first_name: str = "//input[@name='firstName']"
    last_name: str = "//input[@name='lastName']"
    phone: str = "//input[@name='phone']"
    email: str = "//input[@name='email']"
    country: str = "//select[@name='country']"
    user_name: str = "//input[@name='userName']"
    password: str = "//input[@name='password']"
    confirm_password: str = "//input[@name='confirmPassword']"
    submit: str = "//input[@name='register']"
    thank_you: str = "//*[contains(text(), 'Thank you for registering')]"
    post_user: str = "//*[contains(text(), 'Your user name is')]"


class SingOnPage(object):
    """Represent sign on page web element locators."""

    user_name: str = "//input[@name='userName']"
    password: str = "//input[@name='password']"
    login: str = "//input[@name='login']"
    txt: str = "//*[contains(text(), 'Enter your user')]"
    register_link: str = "//*[starts-with(@href, 'mercuryregister.php')]"

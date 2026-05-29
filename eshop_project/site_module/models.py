from django.db import models


class SiteSetting(models.Model):
    site_name = models.CharField(max_length=200, verbose_name='نام سایت')
    site_url = models.CharField(max_length=200, verbose_name='دامنه سایت')
    about_us_text = models.TextField(verbose_name='متن درباره ی ما سایت')
    is_main_setting = models.BooleanField(verbose_name='تنظیمات اصلی')
    address = models.CharField(max_length=200, verbose_name='آدرس ')
    phone = models.CharField(max_length=200,null=True,blank=True,verbose_name='تلفن ')
    fax = models.CharField(max_length=200, null=True,blank=True,verbose_name='فکس ')
    email = models.EmailField(max_length=200, null=True,blank=True, verbose_name='ایمیل ')
    copy_right = models.TextField(max_length=200, verbose_name='متن کپی رایت')
    site_logo = models.ImageField(upload_to='images/site-setting/', verbose_name='لوگو سایت')

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'تنظیمات'

    def __str__(self):
        return self.site_name

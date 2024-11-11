from django.db import models

class BotResponse(models.Model):
    sender = models.CharField(verbose_name='Sender Name', max_length=20)
    user_msg = models.CharField(verbose_name='User Message', max_length=200)
    response = models.TextField(verbose_name='BOT Response')
    polly_file = models.FileField(upload_to='Polly_Speech/')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'Bot Response'
        verbose_name_plural = 'Bot Responses'


    def __str__(self):
        return f'{str(self.pk)} | {self.sender} | {self.user_msg}'


from django_cron import CronJobBase, Schedule

from core.services.mailer.mailer_service import MailerService
from core.models.mail.mail_model import Mail


class SendMailsCronJob(CronJobBase):
    INTERVAL_MINUTES = 1
    MAX_EMAILS_PER_RUN = 6

    schedule = Schedule(run_every_mins=INTERVAL_MINUTES)
    code = 'infotrem.api.cron.send_mail'  # a unique code

    def do(self):
        mails = Mail.objects.filter(sent=False)[:self.MAX_EMAILS_PER_RUN]

        if not len(mails):
            return "[SendMailsCronJob] No e-mail to send!"

        mailer = MailerService()
        mails_sent = 0
        for mail in mails:
            mailer.send_from_mail(mail)
            mails_sent += 1

        return "[SendMailsCronJob] {} emails sent!".format(mails_sent)

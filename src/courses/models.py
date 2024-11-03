from django.db import models


class AccessRequirement(models.TextField):
    ANYONE = "any", "Anyone"
    EMAIL_REQUIRED = "email", "Email required"

class PublishStatus(models.TextChoices):
    PUBLISH = "pub", "Published"
    COMING_SOON = "soon", "Coming Soon"
    DRAFT = "draft", "Draft"



class Course(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    image = ''
    access = models.CharField(
        max_length=10, 
        choices=AccessRequirement.choices, 
        default=AccessRequirement.EMAIL_REQUIRED)
    status = models.CharField(
        max_length=10, 
        choices=PublishStatus.choices, 
        default=PublishStatus.DRAFT)


    @property
    def is_published(self):
        return self.status == PublishStatus.PUBLISH

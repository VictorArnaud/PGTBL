from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.db import models

from appeals.models import Appeal


class Comment(models.Model):
    """
    Appeal comment
    """

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_('Author'),
        related_name='comment'
    )

    appeal = models.ForeignKey(
        Appeal,
        on_delete=models.CASCADE,
        verbose_name=_('Topic'),
        related_name='comments'
    )

    content = models.TextField(
        _('Content'),
        help_text=_('Answer appeal content')
    )

    created_at = models.DateTimeField(
        _('Created at'),
        help_text=_("Date that the comment is created."),
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        _('Updated at'),
        help_text=_("Date that the comment is updated."),
        auto_now=True
    )

    def __str__(self):
        """
        Comment string.
        """

        return self.content[:100]

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')
        ordering = ['created_at']
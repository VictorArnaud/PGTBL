from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from appeals.forms import CommentForm
from appeals.models import Appeal
from core.permissions import PermissionMixin
from disciplines.models import Discipline
from modules.models import TBLSession
from modules.utils import get_datetimes


class AppealDetailView(LoginRequiredMixin,
                       PermissionMixin,
                       DetailView):
    """
    View to show a specific appeal.
    """

    model = Appeal
    template_name = 'appeals/detail.html'
    context_object_name = 'appeal'
    permissions_required = ['show_appeals']

    def get_discipline(self):
        """
        Take the discipline that the appeal belongs to
        """

        discipline = Discipline.objects.get(
            slug=self.kwargs.get('slug', '')
        )

        return discipline

    def get_session(self):
        """
        Take the session that the appeal belongs to
        """

        session = TBLSession.objects.get(
            pk=self.kwargs.get('session_id', '')
        )

        return session


    def get_object(self):
        """
        Get the specific appeal.
        """

        appeal = Appeal.objects.get(
            session=self.get_session(),
            pk=self.kwargs.get('pk', '')
        )

        return appeal

    def get_context_data(self, **kwargs):
        """
        Insert discipline into tbl session context.
        """

        session = self.get_session()
        irat_datetime, grat_datetime = get_datetimes(session)

        context = super(AppealDetailView, self).get_context_data(**kwargs)
        context['discipline'] = self.get_discipline()
        context['session'] = self.get_session()
        context['irat_datetime'] = irat_datetime
        context['grat_datetime'] = grat_datetime
        context['form'] = CommentForm()

        return context
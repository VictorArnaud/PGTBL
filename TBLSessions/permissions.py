from rolepermissions.permissions import register_object_checker
from django.contrib.auth import get_user_model

User = get_user_model()


@register_object_checker()
def monitor_can_change_if_is_teacher(permission, user, view):
    """
    Function to allows only teacher monitors to modify something.
    """

    discipline = view.get_discipline()

    if user in discipline.monitors.all() and \
       user.is_teacher or \
       user == discipline.teacher:
        return True

    return False

@register_object_checker()
def show_sessions_permission(permission, user, view):
    """
    Permission that allows only students, monitors and teacher of specific
    discipline to see discipline session features.
    """

    discipline = view.get_discipline()

    if user in discipline.students.all() or \
       user in discipline.monitors.all() or \
       user == discipline.teacher:
        return True

    return False


@register_object_checker()
def show_tbl_session(permission, user, view):
    """
    Permission that allows only enter in tbl session if its available.
    """

    discipline = view.get_discipline()
    session = view.get_session()

    if session.is_closed and \
       user not in discipline.monitors.all() and \
       user != discipline.teacher:
        return False

    return True


@register_object_checker()
def only_teacher_can_change(permission, user, view):
    """
    Only the discipline teacher can change the student grades
    """

    discipline = view.get_discipline()

    if user == discipline.teacher:
        return True

    return False

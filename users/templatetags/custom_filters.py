from django import template

register = template.Library()


@register.filter
def question_answer_for_qnr(instance, qnr_id):
    return instance.question_answer(qnr_id=qnr_id).yes_no_answer


@register.filter
def question_text_answer_for_qnr(instance, qnr_id):
    return instance.question_answer(qnr_id=qnr_id).text_answer

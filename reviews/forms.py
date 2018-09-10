from django.forms import ModelForm, Textarea
from reviews.models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['first_name', 'last_name', 'rating', 'comment']
        widgets = {
            'comment': Textarea(attrs={'cols': 40, 'rows': 15})
        }

'''<h2>{{ company.name }}</h2>
<h5>{{ company.review_set.count }} reviews ({{ company.average_rating | floatformat }} average rating)</h5>

<h3>Recent reviews</h3>

{% if company.review_set.all %}
<div>
    {% for review in company.review_set.all %}
    <div>
        <em>{{ review.comment }}</em>
        <h6>Rated {{ review.rating }} of 5 by {{ review.first_name }}</h6>
        <h5><a href="{% url 'reviews:review_detail' review.id %}">
        Read more
        </a></h5>
    </div>
    {% endfor %}
</div>
{% else %}
<p>No reviews for this company yet</p>
{% endif %}

<h3>Add your review</h3>
{% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}

<form action="{% url 'reviews:add_review' company.id %}" method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Add" />
</form>
'''

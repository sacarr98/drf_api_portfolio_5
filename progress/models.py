from django.db import models
from django.contrib.auth.models import User

class Weight(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    current_weight = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return f'{self.id} {self.current_weight}'
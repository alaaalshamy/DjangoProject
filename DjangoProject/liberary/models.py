from django.db import models

class Writer(models.Model):
    first_name = models.CharField(max_length=100 , null=True)
    last_name = models.CharField(max_length=100 , null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    contact = models.CharField(max_length=100 , null=True)
    def __str__(self):
      
       
        return '{0}, {1}'.format(self.last_name,self.first_name)    
       
                
    
class Meta:
        ordering = ["last_name","first_name"]

def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('author-detail', args=[str(self.id)])


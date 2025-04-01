from django.db import migrations, models
 
 
class Migration(migrations.Migration):
 
     initial = True
 
     dependencies = [
     ]
 
     operations = [
         migrations.CreateModel(
             name='Pet',
             fields=[
                 ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                 ('name', models.CharField(max_length=100)),
                 ('age', models.IntegerField()),
                 ('species', models.CharField(max_length=50)),
                 ('owner', models.CharField(max_length=100)),
                 ('born_date', models.DateField()),
             ],
         ),
     ]

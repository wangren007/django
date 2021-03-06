from django.db import models

# Create your models here.

class Grades(models.Model):
	gname=models.CharField(max_length=20)
	gdate=models.DateField()
	ggirlnum=models.IntegerField()
	gboynum=models.IntegerField()
	isDelete=models.BooleanField(default=False)
	def __str__(self):
		return "%s-%d-%d"%(self.gname,self.ggirlnum,self.gboynum)

class Students(models.Model):
	sname=models.CharField(max_length=20)
	sgender=models.BooleanField(default=True    )
	sage=models.IntegerField()
	scontend=models.CharField(max_length=20)
	sgrade=models.ForeignKey("Grades",on_delete=models.CASCADE)  #关联外键
	isDelete=models.BooleanField(default=False)
	# def __str__(self):
	# 	return "%s-%d-%d-%s-%d"%(self.sname,self.sgender,self.sage,self.scontend,self.sgrade)
sisi@sisi-X555DG:~/project/ecommerce/src$ python manage.py shell
  File "manage.py", line 17
    ) from exc
         ^
SyntaxError: invalid syntax
sisi@sisi-X555DG:~/project/ecommerce/src$ cd ..
sisi@sisi-X555DG:~/project/ecommerce$ source bin/activate
(ecommerce) sisi@sisi-X555DG:~/project/ecommerce$ cd src
(ecommerce) sisi@sisi-X555DG:~/project/ecommerce/src$ python manage.py shell
Python 3.8.5 (default, May 27 2021, 13:30:53) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from tags.models import Tag
>>> Tag.objects.all()
<QuerySet [<Tag: T shirt>, <Tag: Tshirt>, <Tag: T-shirt>, <Tag: Red>, <Tag: Black>]>
>>> Tag.objects.last()
<Tag: Black>
>>> black = 
KeyboardInterrupt
>>> black = Tag.objects.last()
>>> black.title
'Black'
>>> black.product
<django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object at 0x7f4b9cc09880>
>>> exit()
(ecommerce) sisi@sisi-X555DG:~/project/ecommerce/src$ python manage.py shell
Python 3.8.5 (default, May 27 2021, 13:30:53) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from products.models import Product
>>> qs = Product.objects.all()
>>> qs
<ProductQuerySet [<Product: t-shirt>, <Product: Hat>, <Product: Supercomputer>, <Product: t-shirt>]>
 qs.first()
<Product: t-shirt>
tshirt = 
KeyboardInterrupt
tshirt = qs.first()
tshirt.title
't-shirt'
tshirt.tag_set.all()
<QuerySet [<Tag: T shirt>, <Tag: Tshirt>, <Tag: T-shirt>, <Tag: Red>, <Tag: Black>]>
tshirt.tag_set
<django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object at 0x7f80683297c0>


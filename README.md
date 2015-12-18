# TensorFlow
Samples codes using TensorFlow

Git Operations
==============
Install TensorFlow on Ubuntu without GPU

sudo pip install --upgrade https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.6.0-cp27-none-linux_x86_64.whl

To add files to git
git add .

git commit -m "message"

pull repository
git pull -q

Check models folders in tensorflow directory
============================================

Get Location of TensorFlow installation
vivek@vivek-Lenovo-IdeaPad-U300e:~$ python -c 'import site; print("\n".join(site.getsitepackages()))'

Following are the two location, the package in the second location

/usr/local/lib/python2.7/dist-packages

/usr/lib/python2.7/dist-packages

cd /usr/local/lib/python2.7/dist-packages

Move to tensorflow folder

cd tensorflow

Move to models subfolder

cd models

location of MNIST dataset

/usr/local/lib/python2.7/dist-packages/tensorflow/models/image/mnist

To get MNIST dataset, run the following command in Linux shell

python -m tensorflow.models.image.mnist.convolutional











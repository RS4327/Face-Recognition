{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "44101c0d",
   "metadata": {},
   "outputs": [],
   "source": [
    "from setuptools import setup, find_packages\n",
    "\n",
    "setup(\n",
    "    name='Face-Recognition',\n",
    "    version='0.1',\n",
    "    author='RSR4327',\n",
    "    description='Face-Recognition',\n",
    "    package_dir={'': 'src'},\n",
    "    packages=find_packages(where='src'),\n",
    "    python_requires='>=3.8',\n",
    ")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "92f02dd8",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax. Perhaps you forgot a comma? (1726595812.py, line 12)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[2], line 12\u001b[1;36m\u001b[0m\n\u001b[1;33m    packages=find_packages[]\u001b[0m\n\u001b[1;37m             ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax. Perhaps you forgot a comma?\n"
     ]
    }
   ],
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
    "    url=\"https://github.com/RSR4327/Face-Recognition\",\n",
    "    packages=find_packages[]\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d3887338",
   "metadata": {},
   "outputs": [],
   "source": []
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

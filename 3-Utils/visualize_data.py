# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 23:39:50 2021

@author: talha
"""

import matplotlib.pyplot as plt
def visualize(original,augmented,no):
    plt.figure(figsize=(10, 10))
    fig = plt.figure()
    plt.subplot(3,3,1)
    plt.title('Original image')
    plt.imshow(original[no])
    plt.axis("off")
    for i in range(2,10):
        plt.subplot(3,3,i)
        plt.title('Augmented image')
        plt.imshow(augmented[i-2][no])
        plt.axis("off")
    plt.show()

def visualize_keras(original, augmented):
    plt.subplot(1,2,1)
    plt.title('Original image')
    plt.imshow(original)
    plt.axis("off")

    plt.subplot(1,2,2)
    plt.title('Augmented image')
    plt.imshow(augmented)
    plt.axis("off")
    plt.show()
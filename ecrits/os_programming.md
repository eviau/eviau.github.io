# Getting started in OS programming - a workbook

At RC, I went to a systems programming workshop - and started to think about writing my own, small, operating system as a way to better understand how computers work.

After asking around on the internal Zulip chat, and doing some of my own research, I decided to start this tutorial on Baking Pi by Alex Chadwick, hosted on the Cambridge University website - [here is the link](https://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/os/).

Here are some lessons learned doing that project!

## Rpi now has an imaging utility !

When I first started with the Raspberry Pi some years ago, I was advised to get a microSD card with the OS already installed because doing the installation yourself was uselessly complicated. There is now an [imaging utility](https://www.raspberrypi.org/blog/raspberry-pi-imager-imaging-utility/) that makes this task a breeze!

The way the tutorial works: you need to have an OS already installed on the microSD card of your RPi and then you will compile your OS and upload the resulting kernel image to the microSD card. It feels a bit like a shortcut but it is at my current level of learning about computers, so let’s roll with that.

## Things I like about this tutorial

This tutorial was a great learning experience for me - I got to understand how graphics information is sent to the GPU through a mailbox system and how text information is stored, all of which was lacking in my mostly self-taught programming experience. I got to do a lot of assembly code - still trying to wrap my head around how to think in assembly - which brought back memories of playing [zachtronics games](http://www.zachtronics.com/). Chadwick does an excellent job at explaining at just-the-right-level-of-abstraction what is going on under the hood - and gives you just the right amount of hints to help you get started writing your own code.

Not all the lessons have the answers in them - there are quite a few times where the reader is left to figure things out for themselves. There are available, complete solutions in the Downloads section, so if you are really stuck you can always compare where you are at with these solutions. I think this tutorial was a great code-along experience for a solo programmer. 

## Things to know about the tutorial

I did lessons lesson 0 ( Introduction ) to lesson 07 (Screen02). There is a known bug in lesson 08 that made me skip to lesson 09 to have a fresh code repository. [Here are some notes about this bug](https://www.raspberrypi.org/forums/viewtopic.php?p=828386#p828386) on the raspberry pi forums.

The instructions about installing the USB driver were not clear enough to me to be able to make the lesson 10 work. I am still trying things out for that - let me know by [email](mailto:fleuve.programmation@gmail.com) if you find something!


## References

If you want to know more about how things work - with an historical perspective - you might enjoy this website : https://www.linusakesson.net/programming/tty/

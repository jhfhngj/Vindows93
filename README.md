# Vindows93
Ever stared at Windows93 in fullscreen, thinking to yourself:
> Boy, I forgot I was in a website with the realism! This could be an OS!

Well do I have quite the project for you!



This is Vindows93, a Windows93 OS-layerer-Firefox-placer-scripts-placer-thingymabobber that turns this fun website into a real OS where you have to lean JavaScript and Sys42 to make a program instead of tkinter.

Using Vindows93, you can seamlessly create a nearly done disk image you can flash onto a disk and use instead of Windows 11!

Vindows93 however doesn't patch Windows93 with cool stuff, because I haven't figured out how to yet. Please help me with suggestions for help patching.

The setup process behind the scenes is fairly simple, just a matter of

Fail patching -> grab Tiny Core -> you turn it into directory and pass directory to it -> unpack rootfs -> place stuff -> repack rootfs -> ask you to turn the directory back into an ISO.

And then after that, Vindows93 will boot and it will be good.
Although you need to run some scripts in /home, specifically firefoxInstall.sh, it's mostly seamless!

Installing Firefox is simple, because a Tiny Core forum member, Misalf, has made the firefoxInstall.sh script, and this writes it! Then you run it.

After that you either reboot or run autoFox.sh, both options do the same just rebooting adds a reboot.

Then Vindows93 will have worked!

Vindows93 is still in beta and is being tested.

If patching eventually works there's a configuration generator, setup.html, that generates a config!

And then of course here's a screenshot:

[ASDPASOKDSAD]("https://github.com/jhfhngj/Vindows93/photo.png")

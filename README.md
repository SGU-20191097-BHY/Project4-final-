# Project4-final-

(1)Controls
W ; jump
A : move left
D : move right
R : reload current weapon
1 : switch weapon to pistol
2 : switch weapon to Assualt Rifle(AR)
3 : switch weapon to Sniper Rifle(SR)
Mouse Click : fire current weapon to mouse position.
Mouse Click when icon is red : use “concentration” skill

(2)Rules
1.Player has 500 HP.
2.Zombie have 100 HP.
3.Zombie gets close to player.
4.If zombie is too close to player, player gets 25 damage.
5.Zombie is generated every 0.5 second. At the door.
6.You can kill zombie by weapon.
7.Pistol has 40 damage. Shoot delay is 0.4 second. One magazine carries 12 bullets. Ammo is infinitely provided. Reload time is 1 sec.
8.AR has 30 damage. Shoot delay is 0.1 second. One magazine carries 30 bullets. 150 bullets(include magazine’s) are provided at first. Reload time is 1 sec.
9.SR has 100 damage. Shoot delay is 1 second. One magazine carries 7 bullets. 35 bullets(include magazine’s) are provided at first. SR’s bullet can penetrate 2 zombies. So, one bullet can kill 3 zombies. Reload time is 1.5 sec.
10.Every weapon’s bullet is flying object. Bullet flies from player to mouse-clicked position. If bullet collide with zombie or object(that can step on), bullet disappears(except for SR’s) and zombie get damage.
11.“Concentration” is a skill. 2 conditions should be satisfied to use this skill. (1)It is not in cool down. (2)Mouse cursor is over zombie. If you use this skill, the zombie under the mouse die immediately. This skill ignores walls. Of course, 1 bullet is needed.
12.If you use “Concentration” with SR, skill is activated and one normal bullet flies too. So, you can kill 4 zombies(1 by skill, 3 by normal bullet).
13.Damage done will be added to score. 1 zombie can give 100 score by damage.
14.One zombie kill by normal bullet pluses 100 score.
15.One zombie kill by Concentration pluses 150 score.

---
title: Assignment 2 - Collisions
author:
  - Jon Marien
created: 2025-02-03
published: 2025-02-03
tags:
  - classes
---
| Title                     | Author                       | Created           | Published         | Tags                   |
| ------------------------- | ---------------------------- | ----------------- | ----------------- | ---------------------- |
| Assignment 2 - Collisions | <ul><li>Jon Marien</li></ul> | February 03, 2025 | February 03, 2025 | [[#classes\|#classes]] |
# **Creativity in Physics PHYS13796GD – Simulation #2: Collisions**
*Name: Jonathan Marien | Student ID: 991476393*

1. What are Newton’s three laws of motion?  
	These definitions are straight from my notes -- I hope that is okay -- I write all my own notes based off of your slides/presentations. 
	
>**Newton's First Law of Motion**, also known as the law of inertia, states that an object will remain at rest or in uniform motion in a straight line unless acted upon by an external force.
This law introduces the concept of **inertia**, which is an object's resistance to changes in its state of motion.
**Mass** is a measure of an object’s inertia.

> **Newton's Second Law of Motion** states that the acceleration of an object is directly proportional to the net force acting on it and inversely proportional to its mass.
The relationship is expressed in the equation $F = ma$, where $F$ is the net force, $m$ is the mass, and $a$ is the acceleration.
This means that a larger force produces a greater acceleration, and a larger mass results in less acceleration for the same force.
The acceleration is in the same direction as the net force.
It is important to note that force is proportional to an object’s acceleration, not its velocity.
**Net force** is the total force acting on an object, found by adding all forces, taking directions into account.

>**Newton's Third Law of Motion** states that for every action force, there is an equal but opposite reaction force.
This law highlights that forces come in pairs and that when one object exerts a force on another object, the second object exerts an equal and opposite force back on the first object.
When identifying the forces acting on an object, it is important to consider all the forces, including **weight** (gravitational force) and **normal force** (perpendicular force exerted by a surface).

2. Newton’s Cradle
	a.) Describe what you observe with each of the following seven collision tests:

|     | **Action:**                                                                           | **Description of Results:**                                                                                                                      |
| --- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| *1* | One ball is lifted and dropped at one end:                                            | The single ball transfers momentum through the stationary balls, causing one ball to swing out on the opposite end with nearly identical height. |
| *2* | Two balls are lifted and dropped at one end:                                          | Two balls swing out on the opposite side, mirroring the input.                                                                                   |
| *3* | Three balls are lifted and dropped at one end:                                        | Three balls swing out on the opposite end. Momentum distributes evenly despite the odd number.                                                   |
| *4* | Four balls are lifted and dropped at one end:                                         | Four balls swing out, leaving one stationary ball at the original end.                                                                           |
| *5* | One ball each lifted and dropped simultaneously at both ends:                         | Balls collide at the center and rebound to their original sides.                                                                                 |
| *6* | Two balls each lifted and dropped simultaneously at both ends:                        | Collisions create a "traffic jam" at the center, causing two balls to rebound on each side.                                                      |
| *7* | One ball at one end and two balls at the other end lifted and dropped simultaneously: | Complex interaction where:<br><br>The single ball rebounds weakly (or stops).<br>Two balls swing out on the opposite side with reduced velocity. |
b.) Are the collisions you are observing elastic or inelastic collisions? Explain your answer.
	- Newton's Cradle demonstrates elastic collisions in controlled simulations, as shown by conserved momentum and energy. The collisions in Newton's Cradle are primarily elastic due to the Conservation of Kinetic Energy.$(\Delta\mathrm{KE}\approx0)$ 

3. Collisions: Balls of Different Masses
	Open the ‘Collision Lab’ simulation provided on SLATE and select ‘Explore 1D’.
	- On the menu on the right-hand side, turn off ‘Reflecting border’ and turn on ‘Velocity’ and turn on ‘Values’.
	- Set Masses at bottom of screen as: ball 1 (blue) = 3.00 kg and ball 2 (pink) = 0.10 kg.
	- Click and drag each of the balls so that ball 1 is at position 0.5 m from the left, and ball 2 is at position 0.5 from the right.
	- Click and drag the green velocity vector for each of the balls so that ball 1 has a velocity of 1.00 m/s to the right, and ball 2 has a velocity of 1.00 m/s to the left.
	  
		c.) Record the momentum ($p$) for each of the balls before collision and calculate the total momentum of the system. Remember that ball 2 will be moving in the opposite direction as ball 1, so its momentum is negative.
		![](Assignment%202%20-%20Collisions-February-3rd-2025-18-58-03.webp)
	
	`Ball 1 = 3kg m/s `
	`Ball 2 = -0.10kg m/s`
	
	`Total` $p$ `before collision = 2.9kg m/s`
	
	d.) Click the ‘slow’ button and then click the ‘play’ button to start the collision. After the balls have collided, click the ‘pause’ button to stop the animation.
		[Balls-part-d](Balls-part-d.mp4)
	e.) How have the velocities changed for the two balls after collision?
		`Ball 1 = 0.87m/s`
		`Ball 2 = 2.87m/s`
	
	f.) Record the momentum ($p$) for each of the balls after collision and calculate the total momentum of the system.
		`Ball 1 = 2.61kg m/s`
		`Ball 2 = 0.29kg m/s`
		
	`Total` $p$ `after collision = 2.9kg m/s`
	
	g.) In what direction are the two balls travelling after collision?
		The balls are both travelling towards the right, after the collision.
	h.) How does this simulation prove the Law of Conservation of Momentum?
		I can confirm/prove that the kinetic energy remains nearly unchanged, which confirms that this is an elastic collision.
		Initial State: $$ \begin{aligned}&KE_{\mathrm{before}}=\frac{1}{2}(3)(1.00)^{2}+\frac{1}{2}(0.1)(-1.00)^{2}\\&KE_{\mathrm{before}}=\frac{1}{2}(3)(1)+\frac{1}{2}(0.1)(1)\\&KE_{\mathrm{before}}=1.5+0.05=1.55\:J\end{aligned}$$
		Final State:
		$$ \begin{aligned}&KE_{\mathrm{after}}=\frac{1}{2}(3)(0.87)^{2}+\frac{1}{2}(0.1)(2.87)^{2}\\&KE_{\mathrm{after}}=\frac{1}{2}(3)(0.7569)+\frac{1}{2}(0.1)(8.2369)\\&KE_{\mathrm{after}}=1.13535+0.411845=1.547195\:J\end{aligned}$$
		Energy remains nearly unchanged, 1.55J ≈ 1.547J.
		Total momentum before (+2.90 kg m/s) also equals total momentum after (+2.90 kg m/s), so this simulation proves the Law of Conservation of Momentum.
4. Which of Newton’s Laws of Motion describes Conservation of Momentum and Energy?
	Newton's Third Law of Motion - "For every action, there is an equal and opposite reaction" - describes Conservation of Momentum and Energy. This law explains why when objects collide, the forces they exert on each other are equal in magnitude but opposite in direction, leading to momentum conservation.
5. What would be a real-world application or scenario in which the concept of Conservation of Momentum and Energy and its formulas would be used?
	I can think of multiple practical applications that demonstrate conservation of momentum and energy!
	1. **Vehicle Collisions**
		- Car crash analysis and safety testing.
		- Design of crumple zones and airbag systems.
		- Accident reconstruction investigations
	2. **Space Applications**
		- Rocket propulsion systems.
		- Satellite orbital mechanics.
		- Space debris impact analysis.
	3. **Sports Physics**
		- Billiards/pool ball collisions.
		- Baseball bat hitting a baseball.
		- Ice hockey puck interactions.


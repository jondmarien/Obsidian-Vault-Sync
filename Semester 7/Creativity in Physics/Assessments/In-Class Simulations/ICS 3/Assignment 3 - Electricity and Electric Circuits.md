---
title: Assignment 3 - Electricity and Electric Circuits
author:
  - Jon Marien
created: 2025-03-04
published: 2025-03-04
tags:
  - classes
---

| Title                                            | Author                       | Created        | Published      | Tags                   |
| ------------------------------------------------ | ---------------------------- | -------------- | -------------- | ---------------------- |
| Assignment 3 - Electricity and Electric Circuits | <ul><li>Jon Marien</li></ul> | March 04, 2025 | March 04, 2025 | [[#classes\|#classes]] |

# **Creativity in Physics PHYS13796GD – Simulation #3: Electricity and Electric Circuits**
*Name: Jonathan Marien*
This simulation will examine Ohm’s Law and electric circuits using an online [DC circuit builder interactive](https://www.physicsclassroom.com/Physics-Interactives/Electric-Circuits/Circuit-Builder/Circuit-Builder-Interactive) simulation. Before you begin, answer the following questions to provide a framework of what we will be examining:

1. What are the definitions of **Voltage** (V), **Current** (I), and **Resistance** (R)?
	1. **Voltage (V)**: The electric potential difference between two points in a circuit. It represents the energy per unit charge and is measured in **volts** (V).
	2. **Current (I)**: The flow of electric charge through a conductor, measured in **amperes** (A).
	3. **Resistance (R)**: The opposition to the flow of electric current in a circuit, measured in **ohms** (Ω).
2. What is **Ohm’s Law**?
	1. Ohm's Law states that the **current** ($I$) through a conductor between two points is directly proportional to the **voltage** ($V$) across the two points and inversely proportional to the **resistance** ($R$): $$ I=\frac VR$$Where $I$ is in **amperes**, $V$ in **volts**, and $R$ in **ohms**.
3. What is the difference between a **series circuit** and a **parallel circuit**?
	1. **Series Circuit**: All components are **connected end-to-end in a single path** for current flow. The same current **flows through all components, but voltage divides across them**.
	2. **Parallel Circuit**: Components are **connected across multiple path**s. Each **component receives the same voltage, but currents split** among branches.

## **Part A: Examining Ohm’s Law**

1. Open the ‘DC Circuit Builder’ interactive using the link provided on Slate. Using the ‘Draw’ button that looks like a pencil, create a simple circuit **consisting of a battery, one lightbulb, and wires** connecting everything together. Once everything is connected, you should see the current moving around the circuit.
2. Select the ‘Modify’ button right below the Draw pencil button. It will bring up a magnifying glass over either the battery or the bulb. **Click the battery, which will now allow you to modify the voltage of the battery**. *Change the voltage of the battery to 9.0 Volts*. **Now click the lightbulb to allow you to modify resistance**. *Change the resistance to 5 ohms*.
3. Using Ohm’s Law, what would the current be for this circuit? Remember the units for each of your answers where appropriate!

$$Current =  I=\frac VR=\frac95=1.8\:\mathrm{A}$$

1. We can now add an ammeter to our circuit to confirm this calculation. Using the ‘Draw’ button again, add the ammeter (the structure on the far right of the draw window) anywhere to your circuit. What number is shown in the ammeter once it is added?

Current = ![[Current-Check.png]]

1. To test Ohm’s Law further, complete the table on the following page, either by using the Ohm’s Law formula or by using the simulation (using the ‘Modify’ button to make the corresponding changes to both the battery and the lightbulb to find the current for each of the different variations).

| **Voltage** | **Current at resistance of 5 ohms** | **Current at resistance of 10 ohms** | **Current at resistance of 20 ohms** |
| ----------- | ----------------------------------- | ------------------------------------ | ------------------------------------ |
| 7.0 V       | 1.4 A                               | 0.7 A                                | 0.3 A                                |
| 9.0 V       | 1.8 A                               | 0.9 A                                | 0.4 A                                |
| 12.0 V      | 2.4 A                               | 1.2 A                                | 0.6 A                                |
| 18.0 V      | 3.6 A (Flashing Battery)            | 1.8 A                                | 0.9 A                                |
| 27.0 V      | 5.4 A (Flashing Battery)            | 2.7 A                                | 1.3 A                                |

1. Describe the change in current as voltage is doubled and then tripled in magnitude:
	- When **voltage is doubled** (e.g., from 9.0 V to 18.0 V):
		- For **5 Ω resistance**, *current increases* from 1.8 A to 3.6 A, which is approximately doubled.
		- For **10 Ω resistance**, *current increases* from 0.9 A to 1.8 A, which is also doubled.
		- For **20 Ω resistance**, *current increases* from 0.4 A to 0.9 A, again approximately doubled.
	- When **voltage is tripled** (e.g., from 9.0 V to 27.0 V):
		- For **5 Ω resistance**, *current increases* from 1.8 A to 5.4 A, which is approximately tripled.
		- For **10 Ω resistance**, *current increases* from 0.9 A to 2.7 A, also tripled.
		- For **20 Ω resistance**, *current increases* from 0.4 A to 1.3 A, close to tripled.
	- **Conclusion**:
		- Current is directly proportional to voltage, as predicted by Ohm’s Law ($I=\frac{V}{R}$). Doubling or tripling the voltage results in a corresponding doubling or tripling of the current.
2. Describe the change in current as resistance is doubled and then tripled in magnitude
	- When **resistance is doubled** (e.g., from 5 Ω to 10 Ω at a fixed voltage of 9.0 V):
		- *Current decreases* from 1.8 A to 0.9 A, which is halved.
    - When **resistance is tripled** (e.g., from 5 Ω to 20 Ω at a fixed voltage of 9.0 V):
	    - *Current decreases* further from 1.8 A to 0.4 A, which is approximately one-third.
	- **Conclusion**:
		- Current is inversely proportional to resistance, as predicted by Ohm’s Law ($I=\frac{V}{R}$). Doubling or tripling the resistance results in halving or reducing the current to one-third its original value, respectively.

## **Part B: Series and Parallel Circuits**
1. Using the DC Circuit builder interactive, use the ‘Draw’ pencil button to create a series circuit with three lightbulbs in series and with an ammeter right before each lightbulb. Your circuit should now consist of a battery, three lightbulbs, three ammeters, and wires connecting everything together. Once everything is connected, you should the current moving around the circuit.
2. Using the ‘Modify’ button, change the voltage of the battery to 9.0 Volts and the resistance of each light bulb to 5.0 ohms.
3. Current in a series circuit: what is the current shown by the ammeter in front of your three lightbulbs (again, remember units)?
### Series Circuit
**Bulb #1 = *0.9A*** == **Bulb #2 = *0.9A*** == **Bulb #3 = *0.9A***
4. Based on your values, what can you say about how current flows around a series circuit?
	1. Since it’s a series circuit, current is constant.
	2.  `Bulb #1 = Bulb #2 = Bulb #3 = Total Current.`
5. Voltage in a series circuit: the numbers in the white circles shown around the circuit are voltages, starting with 9 volts leaving the battery. What are the voltage values in front of and behind each of your three lightbulbs (remember units)?
	1. Voltage divides across components:
		Total Voltage = Sum of individual voltage drops.

**Bulb #1 = 27 V** 
**Bulb #2 = 18 V** 
**Bulb #3 = 9 V**

6. Based on your values, what would be the voltage drop across each lightbulb?
	**Voltage drop = 9 V per drop.**
7. Resistance in a series circuit: using Ohm’s Law along with your battery voltage and the current displayed by one of your ammeters in your circuit, calculate the total resistance for your circuit.
	Total Resistance ($R_{total}$) for series:$$ R_\mathrm{total}=R_1+R_2+R_3$$For three bulbs (R=5 ΩR=5Ω): $$ R_\mathrm{total}=5+5+5=15\:\Omega $$Use Ohm’s Law to confirm total current:$$ I_{\mathrm{total}}=\frac V{R_{\mathrm{total}}}=\frac9{15}=0.6\:\mathrm{A}$$
8. Based on this value, what is the relationship between the total resistance of the circuit and the individual resistances of each lightbulb?
	1. Current: Remains constant throughout the circuit.
	2. Voltage: Divides equally among components when resistances are identical.
	3. Resistance: Total resistance is the sum of all individual resistances.
### Parallel Circuit
9. Now change your circuit into a parallel circuit, with three lightbulbs each having their own path as shown below and place an ammeter at the four locations indicated by an arrow on the figure.

![](<Semester 7/Creativity in Physics/Assessments/In-Class Simulations/ICS 3/Attachments/Attachment.png>)
![[image-99.png|308x290]]

10. Using the ‘Modify’ button, change the voltage of the battery to 9.0 Volts and the resistance of each light bulb to 5.0 ohms.
11. Current in a parallel circuit: what is the current shown by the ammeter in front of your three lightbulbs?
	1. Current through each bulb:
		1. Using Ohm’s Law for each branch:$$ I_1=I_2=I_3=\frac VR=\frac95=1.8\:\text{A}$$
	2. Total current (position #1):
		1. Add currents from all branches: $$ I_{\mathrm{total}}=I_1+I_2+I_3=1.8+1.8+1.8=5.4\:\mathrm{A}$$
	**Bulb #1 = 1.8 A == Bulb #2 = 1.8 A == Bulb #3 = 1.8 A**

12. Based on the current from your ammeter in position 1 in the figure above, and your values for each lightbulb, what can you say about how current flows around a parallel circuit?
	1. In a parallel circuit:
        The total current splits among the branches.
        Each branch has its own current, which depends on the resistance of that branch.
        The total current is the sum of the currents through all branches.

13. Voltage in a parallel circuit: the numbers in the white circles shown around the circuit are voltages, starting with 9 volts leaving the battery.  What are the voltage values in front of and behind each of your three lightbulbs?
	In a parallel circuit, the voltage across each branch is equal to the battery voltage:
	- **Bulb #1 = 9 V == Bulb #2 = 9 V == Bulb #3 = 9 V**________________

14. Based on your values, what would be the voltage drop across each lightbulb?
	Since the voltage across each bulb is equal to the battery voltage, the voltage drop across each bulb is: $$ \text{Voltage drop}=\text{Battery voltage}=9\text{ V}$$
15. Resistance in a parallel circuit: using Ohm’s Law along with your battery voltage and the current displayed by the ammeter at position 1 in your circuit, calculate the total resistance for your circuit.
	Total resistance is calculated using the reciprocal formula: $$ \frac1{R_{\mathrm{total}}}=\frac1{R_1}+\frac1{R_2}+\frac1{R_3}$$
	- Substituting values: $$ R_{\mathrm{total}}=\frac1{\left(\frac15+\frac15+\frac15\right)}=\frac1{\frac35}=\frac53=1.67\:\Omega $$

16. Based on this value, what is the relationship between the total resistance of the circuit and the individual resistances of each lightbulb (hint: this relationship is based on the reciprocal of the different components)?
    - The total resistance is always less than the smallest individual resistance.
    - The relationship between total resistance and individual resistances follows the reciprocal formula.

#### Final Summary of Values
| Feature                 | Value   |
|-------------------------|---------|
| Current through each bulb | **1.8 A** |
| Total current           | **5.4 A** |
| Voltage across each bulb | **9 V**   |
| Voltage drop            | **9 V**   |
| Total resistance        | **1.67 Ω** |
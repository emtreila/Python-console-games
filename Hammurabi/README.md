# 👑 Hammurabi
You are the mighty Hammurabi, elected into office for a five year term as ruler of Sumeria. Your goal is to ensure people do not starve, and plant next year's crop. 
Your objective: end your reign with a **prosperous and growing city**.

## 📌 RULES
Each year, you have to decide your policy for city expansion, grain trade, land use, etc.
The currency is the grain unit and time is measured in years. The game lasts for 5 turns (each turn = 1 year).
Each year, you’re shown a status report. Use the data from the report to decide what actions to take.
### Each turn:
- The grain stock is updated.
- People who are not fed will starve (1 unit/person needed)
- Grain used to plant or buy land is subtracted from the stock
- Each person needs 2 units of grain to survive. If not enough grain is supplied, people starve
- If more than half of the population starves during the year, the game is over immediately

### Each Year, You Can:
1. **Buy or sell land**  
   - Land price is random (between 15 and 25 grain/acre)
   - Use grain to purchase, or sell land to earn grain

2. **Feed the population**  
   - 1 grain unit feeds 1 person
   - If not enough people are fed, **they starve** and **cannot plant crops**

3. **Plant crops**  
   - You can plant up to the number of acres you own
   - Each acre needs:
     - 1 person
     - 2 units of grain

###  Environment Simulation
- A random value for **land price** is generated
- **Harvest yields** is calculated based on planted area
- **Rats** may infest grain stocks and eat up to 20% of it
- If not enough grain is allocated for food:
  - People starve
  - If **more than 50%** starve → GAME OVER!
- **Immigration** may occur, growing your population

###  End of game conditions
- The average percentage of people who died from starvation is more than 33% in a year.
- The population drops to less than 50.
- You rule for 5 years and have under 100 people and/or under 1000 acres.

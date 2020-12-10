import getFullBudgetObject from "./9-getFullBudget.js"


const result = getFullBudgetObject(20, 50 , 10)

console.log(result.getIncomeInDollars(result.income))

console.log(result.getIncomeInEuros(result.income))
console.log(result.getIncomeInEuros(1000))
console.log(result.getIncomeInEuros(result.gdp))
console.log(result.getIncomeInDollars(result.capita))

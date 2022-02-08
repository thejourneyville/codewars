function highAndLow(numbers){
  
    converted = numbers.split(" ").map(num => Number(num));
    return `${Math.max(...converted)} ${Math.min(...converted)}`;
  }
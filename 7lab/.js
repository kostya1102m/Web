const uniqueDigitsString = function(...numbers){
    let result = '';
    for (let i = 0; i < numbers.length; i++) {
      const numStr = String(numbers[i]);
      const digits = new Set(numStr); 
      if (digits.size === numStr.length) {
        result += " " + numStr;
      }
    }
    return result;
  };
  console.log(uniqueDigitsString(112,221,123,4,5,55,5,36,3));
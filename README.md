# ICB
Game based on Ice Cold Beer



## Levels JSON
 Generatred on [https://www.json-generator.com](https://www.json-generator.com/) with the following script  

```javascript
[
  '{{repeat(5, 7)}}',
  {
    name : "Level {{index()+1}}",
    target : "hole_{{index()+1}}",
    time_limit : '{{(index()+1) * 60 * 2}}',
    target_time : '{{(index()+1) * 60}}'
  }
]
```
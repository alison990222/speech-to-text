# Conference summarization

we realize this project based on [TextRank4zh](https://github.com/letiantian/TextRank4ZH/).

## Set up
```
$ pip install textrank4zh
```

## Dependence
jieba >= 0.35  
numpy >= 1.7.1  
networkx >= 1.9.1  

## Execute
```
$ python generate.py <file path>
```
we'll get file `result.txt` which saves each paragragh's key words and summarization.

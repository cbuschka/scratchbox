##### http://www.deadcoderising.com/2015-05-19-java-8-replace-traditional-for-loops-with-intstreams/
```
public Optional<Article> getFirstJavaArticle() {  
    return articles.stream()
        .filter(article -> article.getTags().contains("Java"))
        .findFirst();
    }
```

```
public List<Article> getAllJavaArticles() {  
    return articles.stream()
        .filter(article -> article.getTags().contains("Java"))
        .collect(Collectors.toList());
    }
```

```
public Map<String, List<Article>> groupByAuthor() {  
    return articles.stream()
        .collect(Collectors.groupingBy(Article::getAuthor));
}    
```

## collect and exatcly single element
``` 
public static <T> Collector<T, ?, T> singletonCollector() {
    return Collectors.collectingAndThen(
            Collectors.toList(),
            list -> {
                if (list.size() != 1) {
                    throw new IllegalStateException();
                }
                return list.get(0);
            }
    );
}
```

## group with count per group

https://www.mkyong.com/java8/java-8-collectors-groupingby-and-mapping-example/

```
Map<Double, Long> groupByLevel = studentClasses.stream().collect(
            Collectors.groupingBy(StudentClass::getLevel,
                    Collectors.counting()));
```

## flat map (map and combine streams)
```
public Set<String> getDistinctTags() {  
    return articles.stream()
        .flatMap(article -> article.getTags().stream())
        .collect(Collectors.toSet());
}
```



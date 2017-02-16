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

```
public Set<String> getDistinctTags() {  
    return articles.stream()
        .flatMap(article -> article.getTags().stream())
        .collect(Collectors.toSet());
}
```



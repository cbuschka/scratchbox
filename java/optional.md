# Optional

"For return only"

http://blog.jhades.org/java-8-how-to-use-optional/

or

https://dzone.com/articles/optional-java-8-cheat-sheet

## Long form

```
Optional<Customer> optional = findCustomerWithSSN(ssn);
 
if (optional.isPresent()) {
...
} else {
...
}
```

## Short form

```
Long value = findOptionalLong(...).orElse(0L);
```

### with lamda
```
Long value = findOptionalLong(...).orElse(()-> return calculate());
```

## Map
```
int len = opt.map(String::length).orElse(-1);
```

### Map/flatMap

```
Optional<Optional<String>> bad = opt.map(this::tryFindSimilar);
Optional<String> similar =  opt.flatMap(this::tryFindSimilar);
```

## flatMap example impl
```
public<U> Optional<U> flatMap(Function<T, Optional<U>> mapper) {
  if(!isPresent())
    return empty();
  else{
    return mapper.apply(value);
  }
}
```

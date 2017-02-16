#### https://docs.oracle.com/javase/8/docs/api/java/time/package-summary.html

## LocalDate (Day)
```
LocalDate today = LocalDate.now();
```

```
LocalDate tomorrow = today.plus(1, ChronoUnit.DAYS);
```

### Date -> LocalDate
```
LocalDate date = input.toInstant().atZone(ZoneId.systemDefault()).toLocalDate();
```

https://stackoverflow.com/questions/21242110/convert-java-util-date-to-java-time-localdate

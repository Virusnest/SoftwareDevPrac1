from email.encoders import encode_quopri

# SoftwareDevPracTask1

## Task 1: Software Development Practice

Software Dev Class Task 1
- Create a tool to compare Payment Plans over a period of time


## Intersection path Algorithm

Goal: Find the spans of time any given linear equation is smaller than any other

### Algorithm

1. Sort the equations by their y intercepts
2. Starting with the equation with smallest y intercept,
3. Check all the other equations to find the intersection point with the smallest X value
4. Eliminate the starting equation
5. Repeat the process until there are no more equations left or there is no intersection point

### Psuedo Code

```ts
    sort(equations, key="y_intercept")
    currentequation = equations.pop(0)
    spans.append([0, currentequation])
    while (len(equations) != 0) {
        for (i in range(1, len(equations))){
            intersection = find_closest_intersection(currentequation, equations)
            if( list is empty or intersection is None ){
                break
            }
            spans.append([intersection, equations.pop(currentequation)])
        }
    }
```
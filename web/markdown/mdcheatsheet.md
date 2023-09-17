# Heading 1 <!--<H1> in Html -->
## Heading 2 <!--<H2> in Html -->
### Heading 3 <!--<H3> in Html -->
#### Heading 4 <!--<H4> in Html -->
##### Heading 5 <!--<H5> in Html -->
###### Lowest heading level is 6 <!--<H6> in Html -->
####### Heading level 7 does not exist

# Paragraphs   
Just type normally but note;  
ending a line with a double space acts as enter  <!--<br></br> in Html -->
otherwise the lines 
will run
together
like this



*italics*  <!--<i>italics</i>-->  
_also italics_

**Bold**  <!-- <b></b> in html-->  
__also Bold__  
~~is this strikethrough?~~  <!-- <s></s> in html-->  
<u>underline</u>  
<ins> also underline </ins> have to use HTML tags for this


This should be a footnote. [^1].  


[^1]: This should be at the bottom of the page? - does not seem to work in VScode





<!--comment-->

this is for displaying code block - can make it language aware at the top 
<!-- can use python or py to define pythoin formatting -->
```python 
def foo():
    for i in range(3)
        i= i + 1
    return i   
```
```bash
mv project projects
cd ..
rm -rf projects
echo "hello world"
```
or you can do this inline with `for i in numbers;`

~~~
this does the same thing? 
~~~
<!-- for compatibility you should add the | pipes to the ends of the table>

|A| B | C |
|:---:|:---: |:---: |
|table| table | table |
|table| table | table|
|table| table | table |


<!-- unordered list html - list with bullet points
<ul>
    <li></li>
    <li></li>
    <li></li>
</ul> -->
* bullet 
* point
- dash seperates bullet points
   - dash 
+ pluss
+ also
+ work

<!-- ordered list html - list with numbers
<ol>
    <li></li>
    <li></li>
    <li></li>
</ol> -->
1. list
1. list
    1. dsfd
1. list

- [ ] check list
- [x] ticked check


this is how to [insert a link](www.github.com/) into a sentence

![alt text for image](https://placekitten.com/400/200)
<!-- placekitten.com auto generates placeholder images (of kittens) - format placekitten.com/<width>/<height>  -->

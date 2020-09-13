# SOPy - Statement of Python

A package used to make writing SOPs for different programs easier. No more do you have to maintain separate copies and edit each and every one by one when you make minor changes. With the templating system of SOPy, you can write all of your SOPs at once.

## Setup

1. Clone the repository
2. Run the below code from the cloned repo

    ```bash
    pip install -e .
    ```

    or install it from PyPi

    ```bash
    pip install sopy
    ```

## Usage

1. Identify parts of your SOP that would be common for all SOPs
2. Create a folder structure like the following

    ```text
    ├── sops/
    └── templates/
        ├── intro.txt
        ├── remaining.txt
    └── sop.txt
    ```

3. Place all the components that are common for all SOPs into the `sops/templates` folder
4. Create all your main SOP files in the `sop/` folder

Now that we have the basic structure finished, lets take a look at how to populate all this data.

1. **sop.txt**

    This is how you define how your final SOP looks like

    ```text
    {% include "templates/intro.txt" %}

    I really love this program. I will be the happiest person on earth if I get this program. Please let me in. LET ME IN!!!.

    {% include "templates/remaining.txt" %}
    ```

    Notice the text encapsulated by `{% %}`. This is how you would import parts of your SOP. When running the python code, the template engine will automatically import these parts and create the final version of your SOP.

    Also note how you can include templates from subdirectories. You have the freedom to structure the folder however you want.

2. **intro.txt**

    This is the first modular component of your SOP.

    ```text
    Introduce yourself here. Add all the crap about why you wanna pursue graduate studies. Hence, the {{program_name}} and {{university_name}} is the ideal fit for me.
    ```

    Notice the text encapsulated by the `{{ }}`. Here you can define variable names. Usually even though the intro is common for all SOPs, there are some places where you'd wanna mention the university name or what not. So you can define some variable names to fill in later through code.

3. **remaining.txt**

    This is the last part of your SOP.

    ```text
    In conclusion, I wanna study at the {{university_name}}. Blah blah blah, you get the idea.
    ```

    Notice how you can reuse the same variables in different files.

4. Rendering it

    ```python
    from sopy import Document

    sop = Document("sops/sop.txt", template_location="sops")

    sop.render_document(program_name="MS",
                        university_name="Stanford University")

    sop.save_file("final_sop.txt")
    ```

    Note how you can specify where all your templates are in the template_location argument. You don't have to follow the folder structure mentioned above, you can structure it however you want to.

    Running the above python code will render the final version of the SOP after substituting in all the variable names. Heres what the final output looks like.

    ```text
    Introduce yourself here. Add all the crap about why you wanna pursue graduate studies. Hence, the MS and Stanford University is the ideal fit for me.

    I really love this program. I will be the happiest person on earth if I get this program. Please let me in. LET ME IN!!!.

    In conclusion, I wanna study at the Stanford University. Blah blah blah, you get the idea.
    ```

> Note: You aren't limited to creating just two templates. You can create as many templates as you want, just make sure you include them properly in the final SOP file.

## Gizoogle

Are you tired of writing your SOP in a professional manner always? Enter [Gizoogle](http://www.gizoogle.net/). With this tool, you can make your SOP as if Snoop Dog had written it.

Here is the "Gizooglified" version of the above example,

```text
Introduce yo ass here, so peek-a-boo, clear tha way, I be comin' thru fo'sho fo' realz. Add all tha crap bout why you wanna pursue graduate studies yo. Hence, tha MS n' Stanford Universitizzle is tha ideal fit fo' mah dirty ass.

I straight-up ludd dis program. I'ma be tha happiest thug on earth if I git dis program. Please let me in. I aint talkin' bout chicken n' gravy biatch. LET ME IN!!!.

In conclusion, I wanna study all up in tha Stanford University. Blah blah blah, you git tha idea.
```

Here is how you would "gizooglify" your SOP,

```python
from sopy import Document

sop = Document("sops/sop.txt", template_location="sops")

sop.render_document(program_name="MS",
                    university_name="Stanford University",
                    gizooglify=True)

sop.save_file("final_sop.txt")
```

## Credits

This project was in collaboration with ma man [Sourav Johar](https://github.com/SouravJohar/).

# Python: How It Began

## 1989

### **Learning from ABC**

Python borrowed many ideas from ABC, a language for beginners that Guido had helped build at CWI. He kept what worked, like readable code grouped by indentation, and fixed what held ABC back, such as being hard to extend.

- **ABC:** An early programming language designed to be easy for beginners to learn and use. It influenced Python's design.
- **Guido:** Guido van Rossum, the creator of Python.
- **CWI:** Stands for *Centrum Wiskunde & Informatica*. It is a research institute in the Netherlands focused on mathematics and computer science.
- **Readable code:** Code that is easy for people to understand.
- **Indentation:** The spaces at the beginning of a line of code. Python uses indentation to show which statements belong together in a block.
- **Extend:** To add new features or capabilities to a programming language or software.
- **Hard to extend:** Difficult to modify or build upon by adding new features.
- **Influence:** To have an effect on how something is designed or developed.

**Source:** python.org

## 1989

### **Not named after a snake**

Guido named his language after Monty Python's Flying Circus, the British comedy show. He wanted a name that was short, unique and slightly mysterious.

- **Guido:** Guido van Rossum, the creator of Python.
- **Monty Python's Flying Circus:** A British comedy television show known for its unusual humor and sketches. It inspired the name “Python.”
- **British:** Related to Great Britain, which includes England, Scotland, and Wales.
- **Comedy show:** A television program designed to make people laugh.
- **Unique:** Different from others or not common.
- **Mysterious:** Something that is unusual or not immediately easy to understand.
- **Snake:** A legless reptile. Although Python is also the name of a group of snakes, the programming language was named after the comedy show, not the animal.

**Source:** docs.python.org

## 1994

### **Python 1.0**

Python 1.0 came out in January 1994. It added functional programming tools like lambda, map, filter and reduce, contributed by a fan of the language Lisp.

- **Came out:** An informal way of saying that software was officially released and became available to use.
- **Functional programming:** A programming style that emphasizes using functions to transform data and produce results.
- **Lambda:** A Python keyword used to create a small, anonymous function (a function without a declared name). For example, `lambda x: x * 2` returns a function that doubles its input.
- **`map()`:** A function that applies another function to every item in an iterable.
- **`filter()`:** A function that selects items from an iterable when they satisfy a condition.
- **`reduce()`:** A function from Python's `functools` module that combines items in an iterable into a single result by repeatedly applying a function.
- **Iterable:** An object whose items can be processed one at a time, such as a list, tuple, or string.
- **Lisp:** A family of programming languages known for their use of functions and symbolic expressions. It influenced ideas used in many other programming languages.
- **Contributed:** Added or provided something to help develop or improve a project.

**Source:** en.wikipedia.org

## 2000

### **Python 2.0**

Python 2.0, released in October 2000, introduced list comprehensions and a garbage collector that could clean up reference cycles. Its development also became more open to the community.

- **Released:** Officially made available for people to use.
- **List comprehensions:** A concise way to create a new list from an iterable, optionally filtering items or transforming their values. For example, `[x * 2 for x in [1, 2, 3]]` produces `[2, 4, 6]`.
- **Iterable:** An object that can provide its items one at a time, such as a list, tuple, or string.
- **Garbage collector:** A mechanism that automatically identifies and cleans up objects that a program no longer needs, helping free memory.
- **Reference:** A connection from one variable or object to another object in memory.
- **Reference cycle:** A situation where two or more objects refer to one another, directly or indirectly. This can make it difficult to determine whether the objects are still needed.
- **Memory:** The computer space used to store data while a program runs.
- **Community:** The group of people who use, develop, and contribute to Python.
- **Open development:** A way of developing software that makes more of the work, discussions, and decisions visible to the public, allowing community members to participate.

**Source:** docs.python.org

## 2004

### **The Zen of Python**

Tim Peters wrote 19 guiding principles for Python, like "Readability counts". In 2004 they became PEP 20, and you can still read them by typing `import this`.

- **The Zen of Python:** A collection of guiding principles that describe the philosophy behind Python's design and how Python code should be written.
- **Tim Peters:** A Python programmer who wrote these principles.
- **Guiding principles:** Basic ideas or rules that help people make decisions and work consistently.
- **Readability counts:** A principle meaning that code should be easy for people to read and understand, not just make computers perform a task.
- **PEP:** Stands for *Python Enhancement Proposal*. It is a document that describes a proposal, explains a Python feature, or records information and guidelines about Python.
- **PEP 20:** The specific PEP that contains the Zen of Python.
- **`import this`:** A Python command that displays the Zen of Python when entered into a Python interpreter.
- **Python interpreter:** A program that executes Python code.
- **Philosophy:** The set of ideas and beliefs that guide how something is designed or used.

**Source:** peps.python.org

## 2019

### **The Steering Council**

After Guido stepped down, Python's core developers voted for a new model: a five-person Steering Council, elected regularly. The first council, which included Guido, started in 2019.

- **Steering Council:** A group of people responsible for guiding Python's development and making important project decisions.
- **Stepped down:** Voluntarily left a leadership position or role.
- **Core developers:** Experienced contributors who help maintain and develop Python itself.
- **Contributors:** People who help improve a project by writing code, fixing bugs, reviewing changes, or improving documentation.
- **Model:** A system or structure used to organize how something works.
- **Elected:** Chosen through a voting process.
- **Regularly:** At repeated intervals, according to a schedule.
- **Guido van Rossum:** The creator of Python, who stepped down as its BDFL in 2018 but joined the first Steering Council in 2019.

**Source:** peps.python.org

## 2022

### **Faster Python**

Python 3.11, released in October 2022, runs typical programs between 10% and 60% faster than Python 3.10. The speedup came from the Faster CPython project.

- **Speedup:** An improvement that makes a program run faster or complete a task in less time.
- **CPython:** The most widely used implementation of Python. It is written mainly in C and executes Python code.
- **Faster CPython project:** An effort by Python developers to improve CPython's performance so that Python programs run faster.
- **Implementation:** A version of a programming language that makes its rules work in practice. For example, CPython is an implementation of Python.
- **Released:** Officially made available for people to use.
- **10% to 60% faster:** Depending on the program, Python 3.11 could complete certain tasks in less time than Python 3.10. The improvement varies by workload.

**Source:** docs.python.org

## 2024

### **Life without the GIL**

Python 3.13, released in October 2024, added an experimental build without the Global Interpreter Lock. It lets threads run Python code truly in parallel on several CPU cores.

- **GIL:** Stands for *Global Interpreter Lock*. It is a mechanism in Python's standard implementation (CPython) that traditionally allows only one thread at a time to execute Python bytecode within a process.
- **Global:** Applies to the whole Python process rather than just one thread.
- **Interpreter:** A program that executes code written in a programming language, such as Python.
- **Lock:** A mechanism that controls access to a shared resource to prevent conflicting operations.
- **Experimental build:** A version of Python that includes a feature still being tested and developed, so it may not be as mature or widely supported as the standard version.
- **Thread:** A separate path of execution within a program. Multiple threads can help a program handle several tasks.
- **Parallel:** Running multiple tasks at the same time, rather than taking turns.
- **CPU cores:** Processing units inside a computer's processor that can execute instructions. Multiple cores can work on different tasks simultaneously.
- **CPython:** The most widely used implementation of Python, written mainly in C.
- **Bytecode:** A lower-level set of instructions produced from Python code for the interpreter to execute.

**Source:** docs.python.org

# Python People and Fun Facts

## 1995

### **The first BDFL**

The title Benevolent Dictator For Life, or BDFL, is thought to have been first used in 1995 for Guido van Rossum. Ken Manheimer wrote Benevolent Dictator in an email after a meeting. Barry Warsaw added For Life.

- **BDFL:** Stands for *Benevolent Dictator For Life*. In open-source projects, it describes a person who has the final say on important decisions while guiding the community in a friendly and helpful way.
- **Benevolent:** Kind, well-meaning, and wanting to help others.
- **Dictator:** A person who has the authority to make decisions, often without needing everyone’s agreement. In this context, it refers to decision-making authority within a project, not necessarily political power.
- **For Life:** Means that the role is intended to last for the person’s lifetime, although the person can step down.
- **Guido van Rossum:** The creator of Python, who served as Python’s BDFL for many years.
- **Ken Manheimer:** A Python community member who is credited with using the phrase “Benevolent Dictator.”
- **Barry Warsaw:** A Python developer who is credited with adding the words “For Life.”
- **Open-source project:** A software project whose source code is available for people to study, use, and modify under its license.
- **Email:** An electronic message sent over the internet.

**Source:** en.wikipedia.org

## 1999

### **Programming for everybody**

In 1999, Guido van Rossum sent a funding proposal called *Computer Programming for Everybody* to DARPA, a United States research agency. He wanted a language that is easy to read, open source, and good for everyday tasks. These goals still describe Python well.

- **Funding proposal:** A formal plan asking for money to support a project or idea.
- **DARPA:** Stands for *Defense Advanced Research Projects Agency*. It is a United States government agency that supports research into new and advanced technologies.
- **Research agency:** An organization that supports or conducts scientific and technological research.
- **Open source:** Software whose source code is publicly available so people can study, modify, and share it under its license.
- **Source code:** The instructions programmers write to create software.
- **Everyday tasks:** Common activities, such as working with files, processing text, and automating repetitive work.
- **Guido van Rossum:** The creator of Python.

**Source:** en.wikipedia.org

## 2003

### **The first PyCon**

The original PyCon was held in North America in 2003. Today there are PyCon conferences in dozens of countries around the world. PyCon was also one of the first programming conferences to adopt a code of conduct.

- **PyCon:** A conference for people who use and develop Python. The name combines “Python” and “conference.”
- **Conference:** An event where people meet to share knowledge, discuss ideas, and learn from one another.
- **Programming conference:** An event where programmers gather to learn about programming languages, tools, and software development.
- **Adopt:** To officially accept and start using something.
- **Code of conduct:** A set of rules explaining how people are expected to behave and treat one another at an event or within a community.
- **Dozens:** Groups of twelve; in this context, it means many countries.

**Source:** python.org, en.wikipedia.org

## 2013

### **Guido at Dropbox**

In January 2013, Guido van Rossum started working at the file storage company Dropbox. He stayed there for almost seven years. In October 2019, he left Dropbox and officially retired.

- **Guido van Rossum:** The creator of Python, who also worked at Dropbox as a software engineer.
- **Dropbox:** A cloud storage company that lets people store files online and access or share them across different devices.
- **File storage company:** A company that provides services for saving and organizing digital files.
- **Cloud storage:** A way to store files on remote computers accessed through the internet instead of keeping them only on your own device.
- **Software engineer:** A person who designs, develops, tests, and maintains software.
- **Officially retired:** Formally stopped working in a professional career. In Guido's case, he later returned to work in the technology industry, so his retirement in 2019 was not permanent.

**Source:** en.wikipedia.org

## 2020

### **Back from retirement**

On 12 November 2020, Guido van Rossum announced he was coming out of retirement. He joined the Developer Division at Microsoft as a Distinguished Engineer. He later moved to Microsoft's Office of the CTO.

- **Retirement:** The point when someone stops working in their career, often after many years of employment.
- **Developer Division:** A department within a company that focuses on creating and improving software development tools and technologies.
- **Microsoft:** A technology company known for products such as Windows, Microsoft Office, and Azure.
- **Distinguished Engineer:** A senior technical position given to an experienced engineer who provides technical leadership and helps guide important engineering decisions.
- **Office of the CTO:** Stands for *Office of the Chief Technology Officer*. The CTO is a senior leader responsible for guiding a company's technology strategy and technical direction.
- **Technology strategy:** A plan for how a company will use and develop technology to achieve its goals.
- **Announced:** Made information officially or publicly known.

**Source:** en.wikipedia.org

## 2020

### **Language of the year**

The TIOBE index tracks how popular programming languages are. Each year it names a Programming Language of the Year, the language with the biggest gain in popularity. Python won this award for 2020.

- **TIOBE index:** A ranking that measures the popularity of programming languages using information such as search engines, websites, and online discussions. It does not directly measure how much a language is used in real-world projects.
- **Index:** A system that organizes or measures information, often using numbers or rankings.
- **Programming language:** A language used to write instructions that a computer can execute.
- **Programming Language of the Year:** An award given by TIOBE to the language that gains the most popularity in its index during a particular year.
- **Popularity:** How widely known or frequently discussed something is.
- **Gain in popularity:** An increase in how popular something is compared with an earlier period.
- **Ranking:** An ordered list that places items according to a measurement or criterion.

**Source:** en.wikipedia.org

# Built with Python

## 2003

### **Django at a newspaper**

In autumn 2003, Adrian Holovaty and Simon Willison, web programmers at the Lawrence Journal-World newspaper in Kansas, started using Python to build its websites. Their tools became the Django web framework. News deadlines taught them to build websites quickly.

- **Django:** A free, open-source web framework written in Python that helps developers build websites efficiently.
- **Web programmer:** A person who writes code to create and maintain websites and web applications.
- **Lawrence Journal-World:** A newspaper based in Lawrence, Kansas, in the United States.
- **Web framework:** A collection of tools, libraries, and rules that helps developers build websites without having to create everything from scratch.
- **Website:** A collection of related web pages that people can access through the internet.
- **News deadline:** The time by which a news story or newspaper content must be completed and published.
- **Efficiently:** In a way that saves time and effort while achieving a goal.
- **Open source:** Software whose source code is available for people to inspect, use, and modify under its license.
- **Adrian Holovaty and Simon Willison:** The programmers who created Django while working on newspaper websites.

**Source:** en.wikipedia.org

## 2005

### **Mercurial**

Olivia Mackall announced Mercurial on 19 April 2005. It is a distributed version control system written mostly in Python. It was first meant as a replacement tool for work on the Linux kernel.

- **Mercurial:** A free, open-source tool that helps developers track changes to source code and collaborate on software projects.
- **Olivia Mackall:** The original creator of Mercurial.
- **Distributed version control system:** A tool that records changes to files over time and allows each developer to have a complete copy of the project's history on their own computer.
- **Version control:** A way to track changes to files so developers can review earlier versions, compare changes, and restore previous work.
- **Source code:** The human-readable instructions programmers write to create software.
- **Replacement tool:** A tool intended to take the place of another tool.
- **Linux kernel:** The central part of the Linux operating system. It manages hardware, memory, processes, and communication between software and computer components.
- **Open source:** Software whose source code is available for people to inspect, use, and modify under its license.
- **Collaborate:** To work together toward a shared goal.

**Source:** en.wikipedia.org

## 2010

### **Flask, the April Fools' joke**

Flask is a small web framework created by Armin Ronacher. He has said it began as an April Fools' joke that people liked enough to turn into a real project. It is now one of the most used Python web frameworks.

- **Flask:** A lightweight web framework written in Python that helps developers build websites and web applications.
- **April Fools' joke:** A joke or prank made on April 1, traditionally a day when people play harmless tricks on others.
- **Web framework:** A collection of tools and features that makes it easier to build websites and web applications.
- **Armin Ronacher:** A software developer known for creating Flask and other Python tools.
- **Lightweight:** Designed to be small and simple, without requiring many built-in features or extra components.
- **Project:** A planned piece of work, such as developing a software tool or application.
- **Web application:** Software that runs on a web server and is accessed through a web browser, such as an online store or email service.
- **Python web framework:** A framework built with Python that provides tools for handling web requests, URLs, and responses.

**Source:** en.wikipedia.org

## 2010

### **Instagram on Django**

Instagram launched in October 2010, and its web backend was built with Django. It became one of the best-known Django users. Other well-known Django sites include Mozilla, Disqus and Nextdoor.

- **Instagram:** A social media platform where people share photos, videos, and messages.
- **Launched:** Officially released and made available to the public.
- **Django:** A Python web framework that helps developers build websites and web applications.
- **Web backend:** The part of a website or application that works behind the scenes. It handles tasks such as processing requests, managing data, and communicating with databases.
- **Backend:** The part of an application that users usually do not see directly but that makes the application work.
- **Built with Django:** Means Django was used as one of the main tools to develop the website's backend.
- **Mozilla:** An organization known for developing Firefox, a web browser, and other internet-related software.
- **Disqus:** An online service that provides commenting systems for websites.
- **Nextdoor:** A social networking platform designed to connect people with others in their local neighborhoods.
- **Social media platform:** An online service where people create, share, and interact with content.
- **Database:** An organized collection of information that software can store, retrieve, and update.

**Source:** en.wikipedia.org

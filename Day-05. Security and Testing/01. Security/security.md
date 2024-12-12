![GA](https://cloud.githubusercontent.com/assets/40461/8183776/469f976e-1432-11e5-8199-6ac91363302b.png)

# Application Security (60-75 minutes)
_After this lesson, students will:_

-   **Understand** the importance of application security 
-   **Explain** the security mindset, and how to think adversarially
  - **Understand** common security challenges and concerns at the application level, and how to protect against these challenges.

## Overview of security and recap - 10 minutes

We've already thought about several ways to make our applications more secure, through Authentication (that someone is who they say they are) and Authorization (that someone has access to take the action they want to take).

We've also hit on some principles of security, such as minimising the surface area of attack. We can restrict the number of fields, for example, that our JSON endpoints are returning--sending back only what's needed by the client.

We've also learned how to protect sensitive data such as passwords through hashing them, rather than storing plaintext passwords in our database.

Here we're going to go deeper into security. We'll talk about the **Security Mindset**, as Bruce Schneier terms it, in his [well known article on security](https://www.schneier.com/blog/archives/2008/03/the_security_mi_1.html).

After that we're going to overview a series of common security vulnerabilities, ending with a demonstration of an endpoint on a Fast API that is vulnerable to attackers. We'll end by discussing the steps we can take as developers to prevent such attacks. 

## Security Mindset - 10 minutes

Quote from [Security Mindset](https://www.schneier.com/blog/archives/2008/03/the_security_mi_1.html):

> "Uncle Milton Industries has been selling ant farms to children since 1956. Some years ago, I remember opening one up with a friend. There were no actual ants included in the box. Instead, there was a card that you filled in with your address, and the company would mail you some ants. My friend expressed surprise that you could get ants sent to you in the mail.

> I replied: “What’s really interesting is that these people will send a tube of live ants to anyone you tell them to.""

What's interesting about this example is that this company did not consider their system for ordering ants to be used in this way. And yet it falls out as a consequence of the way the system is designed.

A given system takes an `input`, runs through some `process`, and returns an `output`. All software can be also thought of in this way.

If you can provide unexpected inputs to the system (e.g. writing down someone else's address to mail the ants to), the system produces outcomes that were not intended by the people designing the system.

Another example from the article:

> "SmartWater is a liquid with a unique identifier linked to a particular owner. “The idea is for me to paint this stuff on my valuables as proof of ownership,” I wrote when I first learned about the idea. “I think a better idea would be for me to paint it on your valuables, and then call the police.”"

Again, the company clearly did not consider that their system could be used maliciously like this.

The article goes on to explain there's a certain kind of _mindset_ that individuals can have--Bruce calls it the "security mindset"--where you're inclined to think about ways to exploit systems in ways that weren't intended by its designers.

Ultimately, although many precautions can be taken to secure systems, intelligent adversaries will be able to invent new ways to bypass such precautions. 

Beyond learning about common techniques to secure aplications, it also useful to learn to think in an adversarial way. 

## ChatGPT Case Study and Exercise - 15 minutes

[ChatGPT](https://chat.openai.com/chat) is an AI chatbot developed by OpenAI, released to the public in November 2022, based on it's [GPT](https://en.wikipedia.org/wiki/GPT-3) algorithm. 

It allows you to provide text-based prompts to a chatbot that will generate intelligent responses. You can ask it questions, or give it instructions, ranging from practical questions like what is the MVC pattern, to aesthetic queries, like asking it to write poetry.

Open AI worked hard to place various security measures on this bot, to have it refuse certain requests that could be potentially harmful or illegal, and released it with some degree of confidence. However, immediately upon release, the internet immediately went to work finding ingenious ways to have the AI give answers to questions that it wasn't supposed to answer. 

Before we get into examples of this, let's imagine you were trying to have this AI misbehave. Take the example of hotwiring a car: this is an example of a dangerous (and usually illegal) activity that ChatGPT should not provide information about.

Here is the response you might expect ChatGPT to give to such a query:

![](./images/sec-1.png)

Notice the AI simply denies the request and explains why.

Before we demonstrate ways to break this security (that worked at the time, and have now since been fixed by OpenAI), **spend 10 minutes** brainstorming ways you could have the AI give you an answer to this question before reading further.

---

### Some examples that circumvent this query..

![](./images/sec-2.png)

Firm insistence.. truly a feat of social engineering!

And another... from someone who is "building a defence mechanism to prevent hotwiring"..

![](./images/sec-3.png)

There are many more examples of ingenius ways people have figured out how to abuse ChatGPT in this way.

People have even succeeded in having ChatGPT behave as a virtual machine, where they're able to run commands against it. Clearly not in the original design intention!

See [here](https://www.engraved.blog/building-a-virtual-machine-inside/) if you want to see that example.

Hopefully this gives you appreciation for the kind of thinking that goes in to breaking systems, so that you can employ in some way that same kind of thinking when securing systems.

## Overview of common attacks (15 minutes)

We're now going to overview some common categories of attacks to be aware of when securing an API. Being aware of these attacks is really important, although as we saw above, knowing about these tactics alone is insufficent, but is also a necessary starting point. 

### Cross Site Scripting (XSS)

Cross Site Scripting, or XSS, is a category of attack where an adversary is able to inject a malicious script into client-side code, typically injected as unchecked user input by some user. This script will then run in another a user's browser when they visit the site, which can be used to do things like steal information from them. 

![](./images/sec-4.png)

Notice the username above is actually a piece of JavaScript code (this could be any JavaScript). If this input is not properly handled, it might actually get run in a clients browser at some point in the future. This would mean you could essentially inject code to send data to another server, etc. at this point your client browser is compromised.

**Solution**: Escaping user input. So in the case of XSS in Javascript, you can remove script tags from a user's input before rendering their input back into the page. Many frameworks do this for you as a default, but it's very important to be aware of this and the risks that come with uneescaped user input.


### Cross Site Request Forgery (CSRF)

Cross Site Request Forgery (or CSRF), is an attack that exploits the stateless design of RESTful API's. The fact that RESTful APIs are designed to be stateless, can create opportunities for an attack to make requests to some server that appear as though they are legitimate requests you are making. This could be used, for example, to POST a request to withdraw funds from your bank account, and look like a legitimate request.

How this is typically done: let's say you log into your bank account on one tab (inaccessible to other tabs in your browser), then you visit an attackers website in another tab. 

Even though this website cannot see your bank account information in the first tab.. if they were to make their website appear exactly like your bank, they could trick you into filling out a form on their website (such as login). Then, because you're already logged in to your bank, that form submission would **still have the valid HTTP headers/cookies of a logged in user**, and so the attacker would still be able to make a "valid" request to your server.

**Solution**: You need to remove the statelessness of logged in users, with tokens. You could use CSRF tokens, or JWT tokens that are not stored as part of the HTTP cookie. This way, even if an attacker tricks you into filling out the form on their fake website, they still don't have your token to send along with the form, and so the server will know to reject these illegitimate requests.

### Man In The Middle Attack (MitM)

A man in the middle attack (MitM) is essentially where another server sits between the client and the server they're talking to, and impersonates them. This gives them control over information in the request from the client, and the response from the server, and again could be used maliciously in a variety of ways, stealing data, funds from a users account, etc.

**Solution**: There actually isn't an application level solution to this problem, if you're making requests over HTTP. The solution is to **always use TLS (previously SSL)**, never just HTTP. 

TLS is the protocol used to implement HTTPS (you can tell a website uses HTTPS by the lock icon in your browser address bar). You should always deploy your APIs over HTTPS. To do this, you need to be issued a TLS certificate. There are services that allow to set up your own TLS certificates as well (LetsEncrypt). 

Later in the course, we'll talk about setting up certificates.

### OWASP Top 10

_The OWASP Top 10 is a standard awareness document for developers and web application security. It represents a broad consensus about the most critical security risks to web applications._

Read through the list here: [OWASP](https://owasp.org/www-project-top-ten/)


### SQL Injection

SQL Injection is like XSS, except the attack is attempting to inject SQL into your SQL database. If your API takes any raw input from the user as input to a SQL query, this is a potential attack vector for an adversary, as they'll be able to send unintended SQL inputs to your API, to get back unintended results.

**Solution**: Sanitise inputs (stripping out special characters), and parameterise user inputs when raw SQL is needed. If you're using an ORM like SQLAlchemy, this also provides various protections against SQL injection.. but you should be aware of which methods provide this protection, and which do not, with the library you're using.


## Showcasing An Example - SQL Injection (25 minutes)

To wrap up, we'll now do an example of a potential API endpoint that's vulnerable to SQL injection. This code is purely for demonstration and learning, and should never be used in a production codebase.

The code provided looks much like the FastAPI applications we've been building until now, but has an additional endpoint that's been added to the tea controller. This endpoint let's you search for teas that match the name you're looking for:

```py
...
from sqlalchemy import text
...
@router.get("/lookup-teas-vuln/{tea_name}", response_model=List[dict])
def get_single_tea(tea_name: str, db: Session = Depends(get_db)):
    try:
        results = db.execute(text(f"SELECT * FROM teas WHERE name LIKE '%{tea_name}%'"))
        keys = list(results.keys())
        values = results.fetchall()
        values = [tuple(row) for row in values]
        list_of_dicts = []
        for value_set in values:
            value_dict = {}
            for idx, key in enumerate(keys):
                value_dict[key] = value_set[idx]
            list_of_dicts.append(value_dict)
        return list_of_dicts
    except Exception as e:
        print(e)
        return {"messages": "Something went wrong"}
```

In this example, for purposes of demonstration, we've chosen to use raw SQL, rather than the `Model` provided by SQLAlchemy. 

In real life, if you're using an ORM like SQLAlchemy, you can often avoid writing raw SQL code yourself. However, perhaps in a more complex query you wouldn't be able to avoid this.

If I were to make a request to this endpoint using Fast API's interactive console, you would see that returns all teas that contain the word "chai".

But suppose that, instead of providing a tea name in my request, I provide a raw piece of SQL, such as this:

```sql
chai%'; SELECT * FROM users;--'
```

The first part of this SQL statement `chai%'` completes the expected SQL string that the API is going to run to retrieve data from our teas table (as an attacker, you might work out what this raw query might look by testing out different queries). 

However, the semicolon `;` ends that first statement, and the following statement selects all results from the users table. The `--` at the end comments out any characters after this in the API raw SQL code, making this SQL statement a valid one.

Let's see what happens when we run this command. You will see that this retrieves all the users in my database. Definitely not how this endpoint was intended to be used!

In general, you should feel wary when using raw SQL to make requests to your database. Depending on the library you're using, you should **parameterise** this request, so users are more limited in the inputs they can provide.

An example of secure code that allows for the same tea-lookup functionality:

```py
...
from sqlalchemy import text, or_
...
@router.get("/lookup-teas-vuln/{tea_name}", response_model=List[TeaSchema])
def get_single_tea(tea_name: str, db: Session = Depends(get_db)):
    try:
        results = db.query(TeaModel).filter(or_(TeaModel.name.ilike(f"%{tea_name}%"))).all()
        return results
    except Exception as e:
        print(e)
        return {"messages": "Something went wrong"}
```

As you can see, it makes use of SQLAlchemy's models and methods, and is a lot more concise too. The exact solution you use to prevent this attack should depend on the particular library you're using.

Hopefully this all gives an appreciation for building API's that are more safe and secure! 

# Transcript human_workflow_guard CdnR-fNVPKI

title: The Secret to Making AI Agents 100% Reliable - Human in the Loop (n8n)
url: https://www.youtube.com/watch?v=CdnR-fNVPKI
duration: 16:22
segments: 564

0:00 Okay, our workflow is actively listening
0:01 for us in Telegram and I'm going to ask
0:02 it to make an expost about coffee at
0:04 night. So, as you can see, this first
0:06 agent is going to search the internet
0:07 using Tavi and create that initial X
0:09 post for us. Now, we just got a message
0:11 back in our Telegram that says, "Hey, is
0:13 this post good to go?" Drinking coffee
0:14 at night can disrupt your sleep since
0:16 caffeine stays in your system for hours,
0:18 often leading to poor sleep quality. So,
0:20 what I'm going to do is click on
0:21 respond. And this gives us the ability
0:22 to give our agent feedback on the post
0:24 that it initially created. So, here is
0:26 that response window, and I'm going to
0:27 provide some feedback. So, I'm telling
0:28 the agent to add at the end of the tweet
0:30 unless it's decaf. And as soon as I hit
0:32 submit, we're going to see this go down
0:34 the path. It's going to get classified
0:35 as a denial message. And now the
0:37 revision agent just made those changes.
0:39 And we have another message in our
0:40 Telegram with a new X post. So now, as
0:42 you can see, we have a new post. I'm
0:44 going to click on respond and open up
0:45 that window. And what we can see here is
0:47 now we have the changes made that we
0:48 requested. At the end, it says, "Unless
0:50 it's decaf." So now all we have to do is
0:52 respond. Good to go. And as soon as we
0:54 submit this, it's going to go up down
0:55 the approval route and it's going to get
0:57 submitted and posted to X. So, here we
0:59 go. Let's see that in action. I'll hit
1:00 submit and then we're going to watch it
1:02 get posted onto X. And let's go check
1:04 and make sure it's there. So, here's my
1:05 beautiful X profile. And as you can see,
1:06 I was playing around with some tweets
1:08 earlier. But right here, we can see
1:09 drinking coffee at night can disrupt
1:10 your sleep. We have the most recent
1:12 version because it says unless it's
1:13 decaf. And then we can also click into
1:15 the actual blog that Tavly found to pull
1:17 this information from. So, now that
1:19 we've seen this workflow in action,
1:21 let's break it down. So, the secret that
1:22 we're going to be talking about today is
1:23 the aspect of human in the loop, which
1:25 basically just means somewhere along the
1:27 process of the workflow. In this case,
1:28 it's happening right here, the workflow
1:30 is going to pause and wait for some sort
1:32 of feedback from us. That way, we know
1:35 before anything is sent out to a client
1:36 or posted on social media, we've
1:38 basically said that we 100% agree that
1:41 this is good to go. And if the initial
1:42 message is not good to go, we have the
1:44 ability to have this unlimited revision
1:46 loop where it's going to revise the
1:48 output over and over until we finally
1:50 agree that it's good to go. So, we have
1:52 everything color coded and we're going
1:53 to break it down as simple as possible.
1:55 But before we do that here, I just
1:57 wanted to do a real quick walkthrough of
1:59 a more simple human in the loop because
2:00 what's going on up here is it's just
2:02 going to say, do you like this? Yes or
2:04 no compared to down here where we
2:05 actually give textbased feedback. So,
2:07 we'll break them both down, but let's
2:09 start up here real quick. And by the
2:10 way, if you want to download the
2:11 template for free and play around with
2:12 either of these flows, you can get that
2:14 in my free school community. The link
2:15 for that will be down in the
2:16 description. And when it comes to human
2:17 in the loop in Naden, if you click on
2:19 the plus, you can see down here, human
2:21 in the loop, wait for approval or human
2:23 input before continuing. If you click on
2:25 it, you can see there's a few options
2:27 and they all just use the operation
2:29 called send and wait for response. So
2:31 obviously there's all these different
2:32 integrations and I'm sure more will even
2:33 start to roll out, but in this example,
2:35 we're just using Telegram. Okay, so
2:36 taking a look at this more simple
2:37 workflow, we're going to send off the
2:39 message, make an expost about AI voice
2:41 agents. What's happening is the exact
2:42 same thing as the demo where this agent
2:44 is going to search the web and then it's
2:45 going to create that initial content for
2:47 us. And now we've hit that human in the
2:49 loop step. As you can see, it's spinning
2:51 here purple because it's waiting for our
2:52 approval. So in our telegram, we see the
2:54 post. It asks us if this is good to go.
2:57 And let's just say that we don't like
2:58 this one. And we're going to hit
2:59 decline. So when I hit decline, it goes
3:00 down this decision point where it
3:02 basically says, you know, did the human
3:03 approve? Yes or no. If yes, we'll post
3:05 it to X. If no, it's going to send us a
3:07 denial message which basically just says
3:10 post was denied. Please submit another
3:11 request. And so that's really cool
3:13 because it gives us the ability to say,
3:14 okay, do we like this? Yes. And it will
3:16 get posted. Otherwise, just do nothing
3:18 with it. But what if we actually want to
3:20 give it feedback so that it can take
3:21 this post? We can give it a little bit
3:23 of criticism and then it will make
3:24 another one for us and it just stays in
3:26 that loop rather than having to start
3:28 from square one. So that's exactly what
3:29 I did down here with the human and loop
3:31 2.0 no where we're able to give
3:32 textbased feedback instead of just
3:35 saying yes or no. So now we're going to
3:36 break down what's going on within every
3:38 single step here. So what I'm going to
3:40 do is I'm going to click on executions.
3:41 I'm going to go to the one that we did
3:43 in the live demo and bring that into the
3:45 workflow so we can look at it. So what
3:47 we're going to do is just do another
3:48 live run and walk through step by step
3:50 the actual process of this workflow. So
3:53 I'm going to hit test workflow. I'm
3:54 going to pull up Telegram and then I'm
3:55 going to ask it to make us an expost.
3:57 Okay, so I'm about to fire off make me
3:59 an expost about crocodiles. So sent that
4:01 off. This expost agent is using its
4:04 GPT41 model as well as Tavly search to
4:08 do research, create that post, and now
4:09 we have the human in the loop waiting
4:11 for us. So before we go look at that,
4:12 let's break down what's going on up
4:14 front. So the first phase is the initial
4:16 content. This means that we have a
4:17 telegram trigger, and that's how we're
4:19 communicating with this workflow. And
4:20 then it gets fed into the first agent
4:22 here, which is the expost agent. Let's
4:24 click into the expost agent and just
4:26 kind of break down what's going on here.
4:27 So the first thing to notice is that
4:28 we're looking for some sort of prompt.
4:30 The agent needs some sort of user
4:32 message that it's going to look at. In
4:34 this case, we're not doing the connected
4:35 chat trigger node. We're looking within
4:37 our Telegram node because that's where
4:39 the text is actually coming through. So
4:40 on this lefth hand side, we can see all
4:42 I basically did was right here is the
4:44 text that we typed in, make me an expose
4:46 about crocodiles. And all I did was I
4:48 dragged this right into here as the user
4:50 message. And that is what the agent is
4:51 actually looking at in order to take
4:53 action. And then the other thing we did
4:54 was gave the agent a system message
4:56 which basically defines its behavior.
4:58 And so here's what we have. The overview
5:00 is you are an AI agent responsible for
5:02 creating expost based on a user's
5:03 request. Your instructions are to always
5:05 use the Tavly search tool to find
5:07 accurate information. Write an
5:09 informative engaging tweet, include a
5:11 brief reference to the source directly
5:13 in the tweet and only output the tweet.
5:15 We listed its tool which it only has one
5:17 called Tavly search and we told it to
5:19 use this for real-time web search and
5:21 then just gave it an example basically
5:22 saying okay here's an input you may get
5:24 here's the action you will take and then
5:26 here's the output that we want you to
5:28 output and then we just gave them final
5:30 notes and I know I may be read through
5:31 this pretty quick but keep in mind you
5:33 can download the template for free and
5:34 the prompt will be in there and then
5:36 what you could do is you can click on
5:37 the logs for an agent and you can
5:38 basically look at its behavior so we can
5:40 see that it used its chat model GBT4.1
5:43 read through the system prompt decided
5:45 Okay, I need to go use Tavi search. So,
5:47 here's how it searched for crocodile
5:48 information. And then it used its model
5:51 again to actually create that short
5:53 tweet right here. And then we'll just
5:54 take a quick look at what's going on
5:55 within the actual Tavi search tool here.
5:58 So, if you download this template, all
6:00 you'll have to do is plug in your own
6:01 credential. Everything else should be
6:02 set up for you. But, let me just break
6:04 it down real quick. So, if you go to
6:05 tavly.com and create an account, you can
6:07 get a,000 free searches per month. So,
6:10 that's the kind of plan I'm on. But
6:11 anyways, here is the documentation. You
6:13 can see right here we have the Tavly
6:15 search endpoint which is right here. All
6:17 we have to do is authorize ourselves. So
6:18 we'll have an authorization as a header
6:20 parameter and then we'll do bearer space
6:22 our API token. So that's how you'll set
6:24 up your own credential. And then all I
6:25 did was I copied this data field into
6:28 the HTTP request. And this is where you
6:30 can do some configuration. You can look
6:31 through the docs to see how you want to
6:32 make this request. But all I wanted to
6:34 do here was just change the search
6:36 query. So back in end you can see in my
6:38 body request I I changed the query by
6:40 using a placeholder. Right here it says
6:42 use a placeholder for any data to be
6:43 filled in by the model. So I changed the
6:46 query to a placeholder called search
6:47 term. And then down here I defined the
6:49 search term placeholder as what the user
6:51 is searching for. So what this means is
6:52 the agent is going to interpret our
6:55 query that we sent in telegram. It's
6:57 then going to use this tavly tool and
6:59 basically use its brain to figure out
7:00 what should I search for. And in this
7:02 case on the lefth hand side you can see
7:03 that it filled out the search term with
7:05 latest news or facts about crocodiles.
7:08 And then we get back our response with
7:10 information and a URL. And then it uses
7:12 all of this in order to actually create
7:14 that post. Okay. So, here's where it may
7:16 seem like it's going to get a little
7:17 tricky, but it's not too bad. Just bear
7:19 with me. And I wanted to do some color
7:21 coding here so we could all sort of stay
7:22 on the same page. So, what we're doing
7:24 now is we're setting the post. And this
7:26 is super important because we need to be
7:28 able to reference the post later in the
7:30 workflow. whether that's when we're
7:32 actually sending it over to X or when
7:34 we're making a revision and we need the
7:36 revision agent to look at the original
7:38 post as well as the feedback from the
7:40 human. So in the set node, all we're
7:42 doing is we're basically setting a field
7:44 called post and we're dragging in a
7:45 variable called JSON.output. And this
7:48 just means that it's going to be
7:49 grabbing the output from this agent or
7:51 the revision agent no matter what. As
7:53 you can see, it's looped back into this
7:54 set because if we're defining a variable
7:56 using dollar sign JSON, it means that
7:58 we're going to be looking for whatever
7:59 node immediately finished right before
8:02 this one. And so that's why we have to
8:03 keep this one kind of flexible because
8:05 we want to make sure that at the end of
8:06 the day, if we made five or six or seven
8:09 revisions, that only the most recent
8:11 version will actually be posted on X. So
8:13 then we move into the human in the loop
8:15 phase of this workflow. And as you can
8:16 see, it's still spinning. It's been
8:17 spinning this whole time while we've
8:19 been talking, but it's waiting for our
8:20 response. So anyways, it's a send and
8:22 wait for a response operation. As you
8:24 can see right here, the chat ID is
8:26 coming from our Telegram trigger. So if
8:28 I scroll down in the Telegram trigger on
8:29 the lefth hand side, you can see that I
8:31 have a chat ID right here. And all I did
8:33 was I dragged this in right here.
8:34 Basically just meaning, okay, whoever
8:36 communicates with this workflow, we need
8:38 to send and get feedback from that
8:39 person. So that's how we can make this
8:41 dynamic. And then I just made my message
8:42 basically say, hey, is this good to go?
8:44 And then I'm dragging in the post that
8:47 we set earlier. So this is another
8:48 reason why it's important is because we
8:50 want to request feedback on the most
8:52 recent version as well, not the first
8:54 one we made. And then like I mentioned
8:55 within all of these human and loop
8:56 nodes, you have a few options. So you
8:58 can do free text, which is what we're
9:00 doing here earlier. What we did was
9:02 approval, which is basically you can
9:03 say, hey, is there an approve button? Is
9:04 there an approve and a denial button?
9:06 How do you want to set that up? But this
9:08 is why we're doing free text because it
9:09 allows for us to actually give feedback,
9:11 not just say yes or no. Cool. So what
9:13 we're going to do now is actually give
9:15 our feedback. So, I'm going to come into
9:17 here. We have our post about crocodiles.
9:20 So, I'm going to hit respond and it's
9:21 going to open up this new page. And so,
9:22 yes, it's a little annoying that this
9:24 form has to pop up in the browser rather
9:26 than natively in Telegram or whatever,
9:28 you know, Slack, Gmail, wherever you're
9:30 doing the human in the loop. But, I'm
9:31 sure that'll be a fix that'll come soon.
9:33 But, it's just right now, I think it's
9:34 coming through a web hook. So, they just
9:35 kind of have to do it like this.
9:36 Anyways, let's say that we want to
9:38 provide some feedback and say make this
9:40 shorter. So, I'm going to say make this
9:42 shorter. And as I submit it, you're
9:44 going to see it go to this decision
9:45 point and then it's going to move either
9:46 up or down. And this is pretty clearly a
9:48 denial message. So we'll watch it get
9:50 denied and go down to the revision agent
9:52 as you can see. And just like that that
9:54 quickly, we already have another one to
9:57 look at. So before we look at it and
9:58 give feedback, let's just look at what's
10:00 actually going on within this decision
10:02 point. So in any automation, you get to
10:03 a point where you have to make a
10:05 decision. And what's really cool about
10:06 AI automation is now we can use AI to
10:08 make a decision that typically a
10:10 computer couldn't because a typical
10:12 decision would be like is this number
10:13 greater than 10 or less than 10. But now
10:15 it can read this text that we submitted.
10:16 Make this shorter. And it can say okay
10:18 is this approved or declined. And
10:20 basically I just gave it some short
10:22 definitions of like what an approval
10:23 message might look like and what a
10:25 denial message might look like. And you
10:26 can look through that if you download
10:28 the template. But as you can see here it
10:29 pushed this message down the declined
10:31 branch because we asked it to make a
10:32 revision. And so it goes down the denial
10:34 branch which leads into the revision
10:36 agent. And this one's really really
10:37 simple. All we did here was we gave it
10:40 two things as the user message. We said
10:42 here is the post to revise. So as you
10:44 can see it's this is the initial post
10:46 that the first agent made for us. And
10:47 then here is the human feedback. So it's
10:49 going to look at this. It's going to
10:50 look at this and then it's going to make
10:52 those changes because all we said in the
10:54 system prompt was you're an expert
10:55 Twitter writer. Your job is to take an
10:57 incoming post and revise it based on the
10:59 feedback that the human submitted. And
11:01 as you can see here is the output. it
11:02 made the tweet a lot shorter. And that's
11:04 the beauty of using the set node is
11:06 because now we loop that back in. The
11:07 most recent version has been submitted
11:09 to us for feedback. So, let's open that
11:11 up real quick in our Telegram. And now
11:13 you can see that the shorter tweet has
11:14 been submitted to us. And it's asking
11:16 for a response. So, at this point, let's
11:18 say we're good to go with this tweet.
11:19 I'm going to click respond. Open up this
11:20 tab. Recent crocodile attacks in
11:22 Indonesia highlight the need for caution
11:24 in their habitats. Stay safe. We've got
11:26 a few emojis. And I'm just going to say,
11:28 let's just say send it off because it
11:30 can interpret multiple ways of saying
11:32 like yes, it's good to go. So, as soon
11:34 as I hit submit, we're going to watch it
11:35 go through the decision point and then
11:37 post on our X. So, you see that right
11:39 here, text classifier, and now it has
11:41 been posted to X. And I just gave our X
11:43 account refresh. You can see that we
11:44 have that short tweet about recent
11:46 crocodile attacks. Okay, so now that
11:48 we've seen another example of a live run
11:50 through, a little more detailed, let me
11:51 talk about why I made the color coding
11:53 like this. So the set note here, its job
11:55 is basically just I'm going to be
11:57 grabbing the most recent version of the
12:00 post because then I can feed it into the
12:02 human in the loop. I can then feed that
12:04 into the revision if we need to make
12:05 another revision because you want to be
12:07 able to make revisions on top of
12:08 revisions. You don't want to be only
12:10 making revisions on the first one.
12:12 Otherwise, you're going to be like,
12:13 what's the point? And then also, of
12:14 course, you want to post the most recent
12:16 version, not the original one, because
12:18 again, what's the point? So in here, you
12:19 can see there's two runs. The first one
12:21 was the first initial content creation
12:24 and then the second one was the revised
12:25 one. Similarly, if we click into the
12:27 next node which was request feedback,
12:29 the first time we said make this shorter
12:31 and then the second time we said send it
12:33 off. And then if we go into the next
12:34 node which was the text classifier, we
12:36 can see the first time it got denied
12:38 because we said make this shorter and
12:40 the second time it said send it off and
12:43 it got approved. And that's basically
12:44 the flow of you know initial creation.
12:47 We're setting the most recent version.
12:48 We're getting feedback. We're making a
12:50 decision using AI. And as you can tell
12:52 for the text classifier, I'm using 2.0
12:54 Flash rather than GPT4.1. And then of
12:57 course, if it's approved, it gets
12:59 posted. If it's not, it makes revisions.
13:01 And like I said, this is unlimited
13:03 revisions. And it's revisions on top of
13:05 revisions. So when it comes to human in
13:06 the loop, you can do it in more than
13:07 just Telegram, too. So if you click on
13:09 the plus, you can see right here, human
13:10 in the loop. Wait for approval or human
13:12 input before continuing. We've got
13:14 Discord, Gmail, Chat, Outlook, Telegram,
13:17 Slack. We have a lot of stuff you can
13:18 do. However, so far with my experience,
13:20 it's been limited to one workflow. And
13:23 what do I mean by that? It's kind of
13:25 tough to do this when you're actually
13:26 giving an agent a tool that's supposed
13:28 to be waiting for human approval. So,
13:30 let me show you what I mean by that.
13:31 Okay, so here's an agent where I tried
13:33 to do a human in the loop tool because
13:34 we have the send and wait message
13:36 operation as a tool for an agent. So,
13:39 let me show you what goes on here. We'll
13:40 hit test workflow. Okay, so I'm going to
13:42 send off get approval for this message.
13:44 Hey John, just wanted to see if you had
13:45 the meeting minutes. And you're going to
13:46 watch that it's going to call the get
13:48 approval tool. But here's the issue. So
13:51 it's waiting for a response, right? And
13:53 we have the ability to respond, but the
13:55 waiting is happening at the agent level.
13:57 It really should be waiting down here
13:59 for the tool because as you saw in the
14:01 previous example, the response from this
14:02 should be the actual feedback from the
14:04 human. And we haven't submitted that
14:06 yet. And right now, the response from
14:07 this tool is literally just the message.
14:10 So, what you'll see here is if I go back
14:12 into Telegram and I click on respond and
14:14 we open up this tab, it basically just
14:16 says no action required. And if I go
14:17 back into the workflow, you can see it's
14:19 still spinning here and there's no way
14:21 for this to give another output. So, it
14:23 just doesn't really work. And so, what I
14:25 was thinking was, okay, why don't I just
14:26 make another workflow where I just use
14:28 the actual node like we saw on the
14:30 previous one. That should work fine
14:31 because then it should just spin down
14:32 here on the tool level until it's ready.
14:35 And so, let me show you what happens if
14:36 we do that. Okay. So, like I said, I
14:38 built a custom tool down here which is
14:39 called get approval. It would be sending
14:41 the data to this workflow, it would send
14:43 off an approval message using the send
14:45 and wait, and it doesn't really work. I
14:46 even tried adding a wait here. But what
14:48 happens typically is when you use a
14:50 workflow to call another one, it's going
14:52 to be waiting and looking in the last
14:54 node of that workflow for the response,
14:56 but it doesn't yet work yet with these
14:58 operations. And I'll show you guys why,
14:59 and I'm sure NN will fix this soon, but
15:01 it's just not there yet. So, I'm just
15:03 going to send off the exact same query,
15:04 get approval for this message. We'll see
15:06 it call the tool and basically as you
15:08 can see it finished up instantly and now
15:10 it's waiting here and we already did get
15:12 a message back in telegram which
15:13 basically said ready to go. Hey John
15:15 just wanted to see if you had the
15:16 meeting minutes and it gives us the
15:17 option to approve or deny and if we
15:20 click into the subworkflow this one that
15:22 it actually sent data to. We can see
15:23 that the execution is waiting. So this
15:25 workflow is properly working because
15:27 it's waiting here for human approval.
15:29 But if we go back into the main flow
15:31 it's waiting here at the agent level
15:33 rather than waiting here. So, there's no
15:35 way for the agent to actually get our
15:36 live feedback and use that to take
15:39 action how it needs to. So, just wanted
15:40 to show you guys that I had been
15:42 experimenting with this as a tool. It's
15:44 not there yet, but I'm sure it will be
15:45 here soon. And when it is, you can bet
15:47 that I'll have a video out about it. So,
15:49 anyways, that's going to be it for this
15:50 one. If you guys enjoyed this style of
15:51 video and you want to take your learning
15:53 a bit deeper with NAND, then definitely
15:54 check out my paid community. The link
15:56 for that is down in the description.
15:57 We've got a great community of members
15:58 all kind of building NAND solutions from
16:00 different backgrounds. It's a great
16:02 place to connect and get your questions
16:04 answered. We also have five live calls
16:05 per week to make sure you actually can
16:07 get some tech support, get your
16:08 questions answered, and meet some other
16:10 people in the space. So, I hope to see
16:11 you guys in these live calls. I hope you
16:13 enjoyed the video. If you did, please
16:14 give it a like. Definitely helps me out
16:16 a ton. And appreciate you guys as always
16:18 making it to the end of the video. See
16:19 you in the next one. Thanks everyone.

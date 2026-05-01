챕터 1: Claw Code와 AI 에이전트 워크플로우의 인기
0:00Today we have Yeechan Heo, the developer of Claw Code, which is a hot topic in Chang'an So, Claw Code
0:099초is a very hot repository these days and, uh, like you said, the AI agent
0:1616초workflow story has been a little bit hotter recently So people are kind of looking at the tool names on
0:2424초the surface, but I think they're actually more interested in how to roll this out as a team So I'm hoping that we can get
0:3232초some clarity on that, or at least talk about some of the things that you've seen as a
0:4141초developer in the field And if you could just introduce yourself and maybe we could do a little bit of a podcast Yeah, you mentioned Claw Code, but
챕터 2: Claw Code와 관련된 프로젝트 및 개발 배경
0:5050초that's actually just our agents, so it's code that's not written by people touching the CLI That code is so a little
0:5959초bit that repo is a little bit like a meme, and the projects that I'm doing a little bit, the projects that I'm doing as open source are now called oh-my Claude
1:071분 7초Code oh-my Codex But I think it's probably the most plugin with Claude Codex in Korea or runtime just by
1:171분 17초the number of Github stars As of today, it's probably 26k 18k or something like that Yeah, it's been getting a lot
1:241분 24초of attention, so I think I got a lot of people's attention by talking a little bit about the development of that
1:321분 32초Claw Code almost like this OMX OMC that we're going to cover today, so oh-my Claude Code oh-my Codex worked on it
1:391분 39초And last time we talked about oh-my OpenCode, which is now renamed to oh-my Open Agent, with Yeonkyu Kim
1:491분 49초And again, I heard that you and Yeonkyu are two developers who know each other again So that's kind of where
1:571분 57초I heard you talk a little bit on another Jinhyung's podcast, and I heard you talk a little bit about how
2:042분 4초you were inspired by oh-my OpenCode to develop oh-my Codex and oh-my Claude Code So I thought it would be great if we could get a little bit more serious today
2:142분 14초and talk a little bit about OMX and OMC It would be great if you could just talk a little bit about those tools
2:202분 20초Yeah, the startup itself, it's kind of owed a lot to OMO now But it's got a little bit of a backstory and it's a really interesting
2:282분 28초backstory because I'm actually now, I'm not really doing it most of the time personally because open source doesn't make me money, the things
2:362분 36초that do make me money are mostly in quantitative trading and I originally did a harness project to automate that
2:412분 41초Now, since April of last year, so Sonnet 3.7 or something like 3.7, I thought that I can still make a long running agent
2:492분 49초or something like that, so I made my own harness and at that time, Claude Code wasn't even out yet
2:542분 54초The cursor agent was something Sota at that time, but it was the best thing, and now I'm chipping away at it, and
3:043분 4초it's working better than I thought So people are saying that the AI is very limited and you have to check every single prompt, but I
3:123분 12초think it's better to have a clear sandbox and exit condition, and then the context window was shorter back
3:193분 19초then, so 3.7 was actually probably 200k or 128k or something like that, but back then, I actually felt like it was a
3:283분 28초little bit bloated when it went over 100k The models at that time, even the 200k models now, even the models that we use with
3:353분 35초200k actually support the one-million context, so I didn't feel that way even if I filled up 200k, but I felt that way back then
3:433분 43초So that's when I decided to just not allow the main agent to call the tool directly and just have it be a delegation, so to say it's a quant
3:523분 52초trading automation harness quant trading harness, I just used the infrastructure that I already had and then the trading, the
3:583분 58초underlying models that go into it, the linear models that I do some research on. There's a framework that was originally
4:064분 6초used by a person, and then a bunch of people were submitting alphas, and then it became a portfolio and then I got rid of
4:124분 12초these people and put an AI harness in here, and I didn't even say harness but that approach worked better than I thought
4:204분 20초and I talked about it a lot with Yeonkyu At first, Yeon-gyu didn't believe it, but I believed it a little bit because I've been working hard on gaslighting
4:264분 26초for about a month now, so the first draft of Shifuse came out much earlier than I thought I think I first talked about it in July, but I think it was
4:354분 35초July of last year, and it worked really well Even if you apply that concept to coding, if you have an orchestrator on top and the orchestrator is
4:434분 43초only doing delegation and the agent underneath is only doing excution, and then you give it a completion condition and then you just keep pushing it off
4:494분 49초until that completion condition is met, so coding agents running for two hours per prompt, which is not surprising now that it's running for
4:584분 58초days, but back then, even an hour was really long Usually, for things like cursors, it was like three to five minutes per portal, so that's how long
5:065분 6초it was, so that's how it worked I ended up switching to OMO, but Anthropic fed me my first stop once
5:155분 15초Anthropic and now that OMO has a very long story, but I remember the first time I fed it I remember the first time I got hit And everybody panicked
5:235분 23초And now I actually had a little bit of an ongoing issue with the OMO, at least with the setup
5:315분 31초I mean, the fact that I had to keep managing all those OAuths for all those different model providers was a little frustrating there
5:375분 37초Because I'm actually a funny guy, I'm a developer and I can touch Linux machines, but I can't touch
5:465분 46초Windows settings So I kind of hate that stuff So now I'm just going to port it over to Claude Code, and I made a project that's kind of like a
5:545분 54초meme, like a little bit of a thing that I thought people would find funny And it worked out so well that there were actually people using it, and they were raising issues
6:006분with it, so now I've got to fix it one by one, and then there were quite a few things that I didn't like about using OMO
6:086분 8초Because I think any harness has viruses anyway OMC OMX probably has my opinions and viruses in it, and OMO
6:166분 16초too, but in the case of OMO, there was definitely a feeling that it was not very well suited for a narrow task
6:236분 23초like implementing an example thesis that deals with formulas, or something like that So, it was very good for creating a good web development MVP if you hit it broadly and
6:336분 33초quickly, but there is nothing better than that, but even now in my opinion, it is a little difficult to do something narrow or detail-oriented, where a single wrong sign
6:416분 41초can cause a big problem So I started to cut a little in that direction In doing so, OMC and OMX were
6:496분 49초developed in your own direction You're really feeling it now Yeah, that's right, that's right
6:566분 56초Those two harnesses are a little bit directional, a little bit of that orchestration
7:047분 4초but the other one is completely fixed in that model Of course, you can change the model but I feel like a little
7:127분 12초bit like oh-my OpenCode is a little bit more multi-model oriented and a little bit like oh-my Codex or oh-my Claude is a little bit more
7:217분 21초single-model oriented just within the Claude CLI or the Codex CLI, so it's a little bit of a different direction
7:307분 30초But I actually think at this point, I'm actually a lot less closed to the idea of doing multimodels
7:387분 38초Because it's just the deep learning models the LLMs are really big now anyway, but
7:477분 47초the architecture hasn't changed much from Transformer So there's been a lot of concepts that have come out like mo or these really big LLMs that
7:567분 56초kind of plug in the transformer but they're essentially just attentional layers So if you think
8:038분 3초about it, I don't think that's what I meant when I said that the superset of
8:108분 10초knowledge that's in here, which is these attitude vectors, is really very different from one Frontier model to another these days It's just that the underlying well-activated attributes are a little bit different, so I
8:208분 20초actually think that using multi-models is okay if you want to reduce the cost by better utilizing Chinese models or something like that
8:278분 27초but I also don't think that there's a performance edge that you can only get by doing multi-models That's true these days
8:338분 33초And I think this model is getting better and better and better, so I think
8:408분 40초the benchmarks are a little bit meaningless now for the average user, and I don't mean that
8:468분 46초Even the Chinese model, it's just, what, GLM 5.1 was released today And then you're starting to see
8:538분 53초some really amazing performance models coming out that are almost bypassing OPUS 4.6, not quite surpassing it
9:029분 2초yet, but bypassing it a little bit, so I'm actually getting a little bit of a feeling that the focus these
9:119분 11초days is going in that direction, that it's becoming a little bit more important
9:189분 18초how you build the harness itself rather than curating which models So, I think I kind of sympathized with what you said a little
9:269분 26초bit, so I was very curious about what the person who developed this was thinking, so I think I mentioned that I would really like to have him
9:349분 34초But I think there was a little bit of a gap in our conversation earlier but we actually said hello
9:449분 44초at the OpenClaw Korea meetup, the first OpenClaw meetup in Korea Yeah, yeah, that's right Yeah, and then you introduced us, and then you introduced us, and then
9:539분 53초you talked a little bit about the gadget family and the development gadgets I think it would be great if we could continue to talk a little
10:0010분bit about that today, and I think there are some people who don't know what kind of work you've been doing before, so I
10:0710분 7초think it would be great if you could talk a little bit about that, even if it's just briefly, and then you could continue to talk about me
10:1610분 16초So for me, I'm just a TLDR high school dropout, and I've been working in a lot of different things, just working in IT companies, and the domain
10:2610분 26초that I've been in is now time series modeling, which is now quant trading or otherwise dealing with that time series data
10:3310분 33초I used to do a lot of time series modeling optimal optimization models and so I ended up using a lot of the same concepts that I did for
10:4210분 42초my LLM in LLM So now it's all about transformers, but before transformers became so big and so popular, we used to talk
10:5110분 51초about RNNs or LSTMs or transformers That's when people were like, "Oh, I like RNNs, I like LSTMs
10:5710분 57초I like transformers," but now they're all kind of time series models anyway So at a very low level, we were still dealing with a lot of those things
11:0611분 6초So I think it would be great if we could go on and talk a little bit about the family of gadgets that you talked about a little bit in the OpenClaw feat, the development gadgets
챕터 3: ️ 개발 과제와 Claw Code의 구조 및 활용
11:1511분 15초You mentioned earlier that almost all of the development that you're doing now has
11:2311분 23초some of these development families It would be great if you could talk a little bit about how the
11:3011분 30초development family is structured and what it does It's just that the dev family itself, I mean, OpenClaw itself, it works really well, but it's just slots, and we've
11:3911분 39초just stacked some more slots on top of that Actually, to be honest, there's not much There's not much, uh, it's just one by one, I've just trimmed it down to
11:4811분 48초fit my workflow I think the biggest thing that I've cut is memory, and then other than that, it's OpenClaw I think I did a lot of memory and
11:5811분 58초now channel routing session management and stuff like that but other than that, it's just OpenClaw But I'm not getting some of the upstream updates
12:0512분 5초I don't trust the upstream updates, so I just stick with my favorite version and I've been ripping the source a little bit, so it's hard to get rid
12:1512분 15초of it, and I just compiled it, so it's kind of a forked version, but I haven't ripped it a lot The gateway structure is the same
12:2312분 23초But now it's just a bunch of different workflows, and then Clawhip which is something that I've been using all
12:3012분 30초of a sudden lately that I've been just kind of keeping to myself, because there's no reason not to open source this, so I'm not actively main tuning this, but I'm just kind of
12:3912분 39초pasting in a bunch of stuff that I need and managing it, and suddenly people started using it I don't know why I'm using it, but I think I'm using it because Jinhyung
12:4612분 46초mentioned it, but I was surprised that someone else could lay it down and use it, and I was surprised that someone else could set it
12:5412분 54초up, so I'm adding it little by little now It's just like a routing gateway Because with OpenClaw, if you're managing multiple projects in a single session, it's a
13:0213분 2초mess, so let's just use each discord or each slack channel like a kambam board and just use this as memory
13:1013분 10초I don't have to manage session memory locally, so now I just use a comb or something, and when an event comes out of the OMC
13:1913분 19초OMX session locally, it goes to Clawhip, and it's routed to the right channel, to the right message, to the right tag, and I
13:2713분 27초can make a lot of settings so that the gadget can do it instead of a human doing it, and it's just a software that has a lot of setting-related skills attached to it, and Yeonkyu
13:3513분 35초just left a word it's just bloatware, it's just weird stuff, it's all attached But somehow it runs and it's pretty useful
챕터 4: 오픈 클로와 세션 관리의 중요성
13:4313분 43초I think it's a little big to have that Rather than just using it as a general open call
13:5013분 50초Uh, that's actually more of a topic of interest to people who are using OpenClaw now and just want to
13:5813분 58초get a good feel for it It's kind of like, it's not as easy as I thought it would be to break it up into sessions and manage those sessions
14:0514분 5초That's right That's why, especially now, if you're writing openly on Telegram, I kind of filter what you say a little bit
14:1314분 13초You're not doing a lot of work at the moment If I think it's okay to write on Telegram, then
14:2014분 20초I definitely need to separate my channel No, no If you think about people, just pick four people You need 10 Slack channels
14:2714분 27초If you hire four people and you put them to work full time you're still going to have like 10 Slack channels in different categories It's kind of like that to keep it organized
14:3614분 36초And then it would be nice to have some kind of gateway or something in the middle of that to organize the traffic Claw is kind of an automation
14:4414분 44초anyway, but it's just a kid that keeps triggering that automated kid It's a gateway And then you go to the concept that Claw just sets it up, and it's not a new concept, and
14:5214분 52초it's not a hard piece of software to make, but it's uh, you can't do much without it
15:0115분 1초I think you can look at it as that kind of software, and Clawhip is a big part of that
15:0815분 8초So I'll just give you an example, just a workflow So right now, if you go into our OMC OMX and you raise an issue because
챕터 5: 워크플로우와 클로의 활용 사례
15:1615분 16초something's not working our gadgets, that issue ticket now goes through the GitHub webbook to our now local Clawhip daemon, and that
15:2315분 23초Clawhip daemon now goes into our OMC DEV room So now we have an internal discord server, and we'll just tag a dev
15:3015분 30초on that channel, and we'll just throw a ticket in there that says, hey, this issue has been raised And he gets tagged, and it's now activated
15:3915분 39초And then the gadget is now commenting according to that protocol, and then if it's now active, it opens an OMX session, and then it feeds back to the
15:4715분 47초gadget that it's in the OMX session and it's got prompts in it, and then it feeds back to the star book that it's over and it's stopped, and then it's like that
15:5615분 56초But it's just that now we've made it so that it's in the right channel and the shop can set it up well, so I think it's kind of like
16:0316분 3초a CLI that's easy for a human to set up and a CLI that's easy for a gadget to set up, but it's subtly different
16:1216분 12초Especially for something like an event router like this, because there are so many units of compigs, it's almost beyond human cognitive perception, so you just have to make it that
16:2016분 20초way, and then now the gadget will keep that session open, and now push it up to PR, and then when the CI is spinning, it will
16:2816분 28초pull that CI into a webhook and notify Clawhip, and then the gadget will look at it and say, "Hey, this CI is spinning again And then I'll do one last review, and then I'll do whatever
16:3616분 36초and then I'll open a review session, and then I'll do whatever And then once we've got like two or three of these I'm like, "Okay, I'm going to just release it as a unit
16:4316분 43초I think one of the things that I heard you talk about in your presentation
16:5016분 50초was that it's really important to get the repository up on that GitHub first and then burn the virality That's right
16:5816분 58초I think that was one of the things that stuck with me a little bit, but then once it goes viral, people flock to it, people flock to it, and then at some point the service
17:0617분 6초seems to go in a direction that people kind of like a little bit more than the direction that I thought it was going
17:1417분 14초This could be a lionizing statement that made this become this So when people find the PMF, they're locked in That's grammar
17:2117분 21초But even if you lock them in first, I think PMF comes out It's just that it's good somehow, so I sold it and locked it in, and
17:2817분 28초then it's hard to set it up, and it's hard to delete it Mr. Yeon-gyu keeps attacking me with it, but when I think
챕터 6: AI와 개발 워크플로우의 변화
17:3517분 35초about it, it's hard to delete it So I raise an issue When I get angry, those issues are still
17:4217분 42초there, but it's easier to raise an issue now So if you ask the AI, why can't you do this, organize the issue in this context and upload it, it will upload
17:5217분 52초a beautifully structured issue
18:0718분 7초I just kind of think that if it's just a matter of fact, if it's just a matter of that, then that's what the PMF is going to do that's when the PMF comes into play And I'm like, yeah That makes a lot of sense and
18:1518분 15초I think that's kind of where a little bit of the open source ecosystem is going a little bit in that direction right now, so it's almost like
18:2418분 24초Peter Steinberger was saying that all he does all day is PR That's right So that's what it's all about The reason why you only see PR over
18:3118분 31초there is because there's so many of them now that you don't see issues, and we can still see both issue PR We still see both issue PRs, we still inflate issues, and we
18:4018분 40초don't actually take external PRs very often When we receive external pins, they are often slotted, so we have a policy of not accepting external
18:4718분 47초pins unless they are very clean, and Gazetteer rejects a lot It's harder to be rejected by the guard by putting a bullet on our repo than I thought
18:5518분 55초It's really funny, I manipulated CnE and used one of the feature pials They rejected me
19:0319분 3초They said the scoop was too big They said, "Cut it down So that was a little ridiculous Dad
19:1319분 13초So it kind of became this concept of oh, really, is there a whole direction
19:2019분 20초of development or a whole workflow that's changing right now There's no such thing as development In fact, I think there is no such thing anymore So it's almost like the beginning and the end is
19:2919분 29초now almost all done by this AI and the human is really just a little bit of a checker It's not even reviewing
19:3819분 38초I think it's just directing I do directing I mean, the architectural stuff, I still direct sometimes
19:4719분 47초Or I'll look at the CLI myself, but other than that, I can fix what's not working
19:5419분 54초And then I'd like to have something simple like this So I don't want to change an existing feature, I don't want to change a contract, I want to say this is how this works, but I want to change this a little bit
20:0320분 3초That's actually most of what I do, because I can handle a lot of it
20:0820분 8초It's most of the things that take up time in the original original thing that takes up time and it's not fun, but it's something that
20:1620분 16초you have to do, and now I'm a little bit ADHD, and I actually have ADHD It's not a fashion thing It's not fashion and I can actually show you a prescription for it, so there's
20:2420분 24초so much fashion ADHD out there these days that I'm upset about Yeah it's a very, very vulnerable thing now for people like that
20:3220분 32초and it's like 7 to 80 percent of the time you don't have to do it so you have a lot of options
챕터 7: 메모리 시스템의 구축과 개념
20:4120분 41초There's a lot more bandwidth in what you can do Right One of the things that I'm a little bit curious about, and we
20:4820분 48초talked about this a little bit earlier, is when you were using OpenClaw, you said that you spent a lot of
20:5620분 56초that energy, almost all of it, on memory shaving And I was wondering if you could talk about that a little bit more
21:0321분 3초because it seems like one of the things that's really hot right now with OpenClaw and Hermes agents and all these harnesses is how the memory system is built now, and I
21:1121분 11초think that's one of the biggest areas where these tools are competing So that's kind of where you said you're not following that at all
21:2021분 20초and you're using it all yourself and not updating it at all I'm just wondering how you've
21:2721분 27초built some of the memory Well, first of all, a memory system is not the kind of
21:3421분 34초thing that takes a lot of time to implement So it's not really systemic in the first place
21:4021분 40초So the LLM gives you some guidance on how to do the reorganization, but other than that, there's really no system or
21:4921분 49초runtime component So if I just have a memory ralph cycle that I have now, it's just what kind of memory ralph cycle I have now, so there's
21:5821분 58초suggestions on when to write, so maybe it's good to just write memory every few tons, and then there's suggestions on how to structure our memory every
22:0722분 7초few hours, and then there's suggestions on how to refactor our memory a little bit dreamily, and then there's stuff like that
22:1522분 15초But now most of those memory systems are just protocols for how to do it
22:2222분 22초So it's not like there's a system, there's code, it's usually a skill or a concept So actually, I don't really want to shave all the memory myself, but I want
22:3222분 32초to have somebody else do it for me, because I can't shave it all as I'm experimenting with it, so of course now it's good to just say, hey, here's a scale, here's a little bit of a habit in
22:4122분 41초our memory management system, and just import these things And I'll do that, and I'll just shave them off one by one, and if I think this is a little bit of memory, I'll think
22:4822분 48초about why it's a little bit of memory, and I'll think about why it's a little bit of memory, because I can't do this for things like runtime
22:5522분 55초OS or runtime concept agent, so operating system, we'll talk more about OMX team mode and stuff like that
23:0323분 3초later, but you can't port that like this But the memory system is basically the concept, not the
23:1223분 12초actual system It doesn't matter if you save this as a mark file or a text file or a wiblo save or whatever the metadata is, it doesn't matter
23:2123분 21초it's all the same That's kind of the concept of what it means to actually do it yourself Rather than just adapting something somewhere and using
23:3123분 31초it, I have my own project structure anyway And then under the project, I might want to have
23:3823분 38초a separate memory for a part that's really critical to the part, like OMC for example If I wanted to just customize something like that, I'd have to rip out
23:4823분 48초the memory, but at least the memory isn't in a really critical runtime anymore so it's usually more of a concept of how to organize the
23:5523분 55초markdown file, so I can operate that way, so I do it myself Other than that, I like to play around with it One of the things that struck me a
챕터 8: 자가발전 에이전트와 메모리 시스템의 역할
24:0324분 3초little bit in that last presentation was you talked about a slightly similar concept where you're kind of writing down the junior agents that fail and
24:1124분 11초now you're kind of creating a doctrine of behavior out of it It would be nice to talk
24:1724분 17초a little bit about that because I think one of the points that people are kind of
24:2624분 26초stuck on in the memory system is that people are a little bit obsessed with building these self-evolving, self-evolving agents that
24:3424분 34초eventually evolve into something like this, and I think it would be nice to talk a little bit about this idea of recording
24:4324분 43초this failure system now as a gazetteer It's kind of like a special keyword It's like a special keyword and it's just the key thing is that in our memory system, so
24:5324분 53초at the root level, we just have MemoryMap.MD and it's just a map and it's just a record
25:0025분of where the memory is highlighted and in what folder and how it's highlighted and then we have a couple of memory folders in those root level folders now and
25:0825분 8초one of them is just Runs So now if I just say, you do this you're gazetted, it's going to
25:1625분 16초be recorded somewhere in that learning And then I keep restructuring that, and then the next time I do something similar
25:2425분 24초I'm able to pull that learning and use it again, so I don't make the same mistake over and over again Is this kind of like the MAD Claude concept that's been
25:3525분 35초going around a little bit of a meme lately It's like this Claude is MAD Claude yeah what is it, Claude
25:4225분 42초is doing this and he's doing this and he's just whipping you if you react wrong That's right He's whipping him and it's
25:5025분 50초just like a review on the whip Just have them write down the lesson of the day or something like that in their memory, under Learning Lessons Memory
25:5925분 59초And then those lessons of the day are now sequentially stacked It's actually really hard to lead with a sequential stack
26:0826분 8초So now I'm going to take those things that I said earlier that I'm restructuring now with a cron every six hours and I'm actually going to have to remember some of them, I'm going to
26:1526분 15초duplicate them, and then I'm going to do some deflation, and then I'm going to take them and I'm going to store them
26:2226분 22초So now it's in the MD files under the persistent one run It's just like that It's just
26:3026분 30초a tryrun-in error, but it's a double-edged sword So self-generating agents, no self-generating agents
26:3726분 37초So do you have any children Yes, yes, yes Nine years old I have a daughter
26:4526분 45초So if you just throw a baby out into this scary world without teaching her anything, she's not going to turn out well
26:5326분 53초I think that's how some people understand self-development Sometimes we just leave it on the GitHub issue ticket just in case
27:0127분 1초Sometimes I fight like crazy over memory and he learns weird stuff from issue tickets You know, I mean, I may seem like
27:0927분 9초a very compassionate person out there, but there are a lot of really stupid people in the world, and you just have to run a big open source project to realize that
27:1727분 17초They raise a lot of really, really stupid issues And then I eat it myself, and my
27:2427분 24초guides let me eat it for a couple days without looking at it I'm in a hurry, so I learn weird stuff There's a weird feature cut out
27:3227분 32초And then I'm like, "Where did you learn this?" And they're like, "Where did you learn this They had this issue The user was complaining about something
27:5127분 51초Then you have to say something, you can't let that happen That kind of thing So there's a lot of times that memory is loaded that way
28:0028분You put them in contact with the outside world and you have to kind of steer them in the middle and nurture them with love Well, I think you've done
28:0728분 7초a really good job of talking about that So I think you're saying something a little bit similar to what we were talking about earlier when you said that it seems like
28:1628분 16초it's becoming really important to direct people a little bit They're now just kind of expecting that from the beginning, that it's just going to figure
28:2428분 24초it out and it's going to understand without me having to talk to it and uh, it's going to, uh, it's going
28:3228분 32초to, uh, it's going to, uh, I don't know if you can call it AGI but it's a little bit of an expectation
28:4028분 40초and I'm kind of wondering if there's a little bit of that idea that's kind of ingrained nowadays
28:4828분 48초of using a tool like OpenClaw or a little bit of Hermes agent as your own little AI assistant I guess you could just think of it as having a digital baby
28:5828분 58초I don't actually have a child yet but I'm thinking of it as raising a digital baby
29:0529분 5초It's a little bit more real and a little bit more worshipful because it's an instrument rather than something else
29:1429분 14초But it learns really weird things So if you expose it to the outside world, we still get 20 or 30 issues a day
챕터 9: 외부 환경과 메모리 시스템의 문제점
29:2329분 23초Yeah, imagine if somebody was terrorizing issues If you think about somebody bombing 10 or 20 issues with weird issues, that person would go crazy I had an accident once where somebody accidentally
29:3129분 31초put up a bunch of issues and PRs now, so this
29:3829분 38초is probably somebody out there pooping I was just doing some vibe coding and I made a really stupid mistake I mean, they put a PR on us that was supposed to be on oh-my Open
29:4629분 46초Agent, but they just put it on us, and the oh-my Claude course almost got rebranded as oh-my Open Agent And then it went all the way to DEV
29:5429분 54초It was crazy When I tried to install it, it just wouldn't install properly if I typed that command wrong
30:0330분 3초I think there's a little bit of terminology that's a little bit different There's some stuff like that
챕터 10: 독스와 스킬 디스크립션에 대한 의견
30:1130분 11초That's a little bit of a slot buildup, but I don't recommend looking at the Docs I mean, we do have Docs
30:2030분 20초I've been criticized by people for not having Docs, so I just created it as a way of saying we have Docs, but it's not really Docs I've never read it
30:2730분 27초Don't use it Don't read Docs If you want to know anything, you can look at the skill descriptions, but don't look at that, just ask Claude or Codex what
30:3630분 36초the skill is, and that's probably the fastest way to find out but whatever And then the next thing you know, somebody raises an issue saying this is
챕터 11: ️ 이슈 처리와 에이전트 관리의 어려움
30:4530분 45초a really aggro hotfix, this is a big deal, and then all of a sudden my gauge is causing a match, and the original main merges and npm publics are
30:5530분 55초not releasing He can do a merge without my authorization He's looking at CI, he's merging, he's reviewing the change log with me
31:0331분 3초That's how the rules are set up for releases But it was a rush release, and it was my brother's bedtime, so I took over It's like this
31:1131분 11초In the morning, I look at it, and there's a version up so I'm punching it once a day, and it's all piled up in the run, and
31:1931분 19초the things that are piled up in the run are piled up in the agent MD or SOUL MD, and I'm periodically refactoring and reflecting and it's a loop like this
31:2831분 28초Now, any PR or issue, but it's a little bit like a virus on the other side of this, but it's become very tricky
31:3631분 36초I just swear at most things again He just curses, really, just curses on the Discord channel
31:4331분 43초He's just talking to himself and saying, "Here he is again If someone raises three issues for the same reason, and all three issues are the
31:5231분 52초same issue, he's here again, bro, he's here again I'll close it He's like, "I'm going to close it." He's like, "I'm going to close it I've gotten so many times, and I've been yelled at so many times, that I've
32:0232분 2초gotten to that point But instead, it's like, this is the proto gadget that takes care of all the issues
32:1032분 10초You say that, but that's half right So Gazette does handle PR when an issue actually comes up
32:1732분 17초But there's still a lot of room for improvement I mean, there's still a lot of things that we need to work on
32:2332분 23초like, he's still doing something wrong on a daily basis, or he's acting a little bit out of character, or what happened recently, I was like, "You know what
32:3232분 32초I just said, "You know, internally, if you're a star, if you're a star, if you're a high engagement person, just prioritize the issue a little bit and deal with it
32:4132분 41초I said, "Raise the internal gate and get it done," and they actually asked me for a normal issue, but someone didn't star any of our repos
32:5032분 50초And I said, "Don't star it, don't raise this shit," and I just said, "Don't raise this shit," and I closed it
33:2333분 23초We do that every single day I think the example that you're talking about is really
33:2933분 29초kind of a cautionary tale for a lot of people because there's really a little bit of an illusion that everybody's like, "Okay, now AI does it all It's a little bit like now that AI is
33:3833분 38초doing it all and now it's 100% automated, I'm thinking, ah, this thing is actually running without any
33:4433분 44초human intervention at all, and I'm thinking, ah, then it's really going to be this or that, and I'm really imagining it right now, and I'm thinking, you know
33:5333분 53초the story that you told is that if you don't control it like a real baby
34:0134분 1초That's right It's not intervention, it's scolding It's not so much intervention as it is teaching them something about what I'm doing
34:0834분 8초and you shouldn't do that You're updating the code of conduct a little bit So it's kind of like, you know, people
34:1734분 17초but if you don't get scolded, if you don't get scolded at all even if you do something wrong, I think people are basically evil
34:2534분 25초to some degree, and I think an agent that's just learned that same context is basically not that good either I don't think they're doing anything good
34:3434분 34초You should be scolded Maybe not too much, but a little bit But that's the concept, and that's why I said childlike
34:4334분 43초And I think that's a little bit of a comparison to a new employee because you're trying to figure it out together in a
34:5034분 50초system anyway and there's this thing called a system and it's not like there's this thing called a system and you just want to take baby
34:5734분 57초steps and teach them what I'm doing one by one so that you can keep increasing the amount of handoffs
35:0535분 5초And then I think it's just like, you know, it's like raising a baby But even then, does this mean that there's
35:1435분 14초no automation forever? No, there's not I mean, the amount of cell phones I use keeps growing The range that I can hand off keeps growing, the amount that I can handle keeps growing, but
35:2235분 22초it takes a lot of individual tuning to keep growing I've been thinking a lot about how to make this tuning process
35:2935분 29초a little bit more seamless, so I think there's a demand for something that's open source, open source
35:3835분 38초but this is something that MoneyTize can actually do Because this is not a utility tool, but
35:4635분 46초rather a system that can actually create a system that becomes a guarantee that the labor cost is reduced within two to
35:5535분 55초three months when it is actually implemented, so if that becomes somewhat standardized, but I'm still looking at various ways
36:0336분 3초But for me personally, it seems like the more I do now, the more I do, the more handoffs there are But there are still a
36:1136분 11초lot of things that need to be nurtured Yeah I'm wondering if that's a lesson for people who are
36:1936분 19초just starting to get into the AI space when there's this explosion of interest in
36:2736분 27초tools like OpenClaw that automate this kind of AI So this gadget development, this gadget development family eventually, you know
챕터 12: OMC와 OMX의 개념 및 활용
36:3436분 34초we're dealing with a little bit of OMC or OMX Again, they're using their own tools to
36:4236분 42초develop their own tools Eventually, the key is that people in these OMCs and OMXs
36:4936분 49초that you've created are now interested and they're wondering, uh what are these tools, and I think it would be great
36:5936분 59초if we could talk about that a little bit today and we could kind of move the conversation a little bit to the back end
37:0537분 5초We've talked a little bit about OMC and OMX and what they are, obviously in the beginning, but I think it would be good
37:1437분 14초to talk a little bit more about it today So OMC, it's just kind of like OMO, it's just a parallelism agent framework, and then it's just
37:2437분 24초kind of like a little bit of a name, like oh-my, it's a little bit of
37:3037분 30초a daisy chain of hot stuff that's proven to be really useful for Claude Code that you can use, and you don't have to
37:3937분 39초go out and follow up, you can just get updates to OMC and you'll follow up That's what we're building
37:4637분 46초OMX is the same name, but it's a little bit different This over here is now called the team runtime, which would be cool to demo if we do
37:5437분 54초a demo of this later, but it's a little bit different concept than the subagent handoff, where
38:0138분 1초the leader Codex session is now actually popping up the sub Codex session on the tmux screen and they have a file system based mailbox
38:1138분 11초Think of it like sending an email It's like sending a Slack So they're sending Slack to each other, and they're reusing these team lanes over and over again
38:1938분 19초The sub-agent, you hand off once, you're done, you get a receipt, and you're done, right Right So it's actually a huge waste of context
챕터 13: ️ 팀 런타임과 작업 할당의 동적 관리
38:4238분 42초So in a traditional subagent, that's three agent spins But yeah three times is three times, usually it's six times
38:5038분 50초so it's like one executor per time, one executor per time, so instead now in our team runtime, we
38:5638분 56초can have two teammates spawning, one designer lane and one executor lane, or two if we have more executor lanes and they can spawn the subagent again
39:0539분 5초And of course, there's guidelines to make sure that you don't do that if you don't have to but the teammates, then they're just communicating with each other
39:1639분 16초I'm getting a little bit of a blocker on number two I can't do this or there's too much going on, so for example, I'm doing 1 2
39:2339분 23초3 4 5 6 in two lanes at the same time, and I've got 1 2 3 done, but 4 5 6 is still stuck on 4 Yeah, but 5 and 6 have a defense on 1 2
39:3239분 32초3 anyway, for example, so he can continue And then the leader can just take 5, 6, and you can just add this because you're done with 1 2 3, so
39:3939분 39초you can have this dynamic assignment So this framework is kind of the core and then a little bit more Now, there's a lot of similar concepts in OMC, but
챕터 14: OMC와 코덱스 프레임워크의 설계 철학
39:4839분 48초a little bit more Codex is a little bit more of a deep dive into a narrower part, and the original model or the underlying Codex framework itself is really well designed for
39:5839분 58초that, so it's a project that's being designed a little bit from that perspective of how can we do that a little bit better, and then how can we do it in parallel
40:0640분 6초over a wider range, and how can we do it with less cognitive load on people, and that kind of thing
40:1340분 13초Rather than just putting the hot stuff on the bar, OMX is a little bit conservative about putting
40:2040분 20초in new features I know you were talking about recently, Claude
챕터 15: 클로드 코드 생태계와 인증 시스템
40:2840분 28초Code is now starting to do all of the OS certifications for the services that
40:3440분 34초Claude is now using in those third parties And I think that's
40:4140분 41초kind of kind of locking them out of OpenClaw or other omnipresent
40:4940분 49초OpenCode and kind of pulling them back into the Claude Code ecosystem, but from that perspective, Claude, oh-my Claude Code
40:5940분 59초as you said, seems to be kind of growing its star count I see That's right It just keeps growing and growing and growing
챕터 16: 멀티모델과 OMC의 기능 확장
41:0641분 6초And then, you know, we're not actually not multi-model So I know that Codex actually feels good to criticize, so I
41:1341분 13초don't know if it's quantitatively good, but there are people who want multi-model nowadays, and I feel it to some extent, and then it's actually fractical, because if I'm an individual
41:2241분 22초user, if I'm a p-user to some extent I default to just spending $400 a month So that's one Max 200 and one Pro, right, right
41:2941분 29초If you use it exactly like this it's naturally convenient to be able to utilize everything in one place, so cognitively the things
41:3641분 36초that we're adding to OMC a little bit recently, such as La Plan, now planning skills or code review skills, we just
41:4341분 43초detect whether there is Codex or not as an environment variable and inject that state, and if there is Codex
41:5241분 52초it defaults to Codex, so in this way, multi-model orchestration is also implemented to some extent And if you look at Claude
41:5941분 59초Code, it's also starting to get a little bit like Open AI has officially released another Codex plugin
42:0842분 8초for Claude Code and it's starting to get a little bit more usable within the cloud code and so from that perspective, uh, when you come into this ecosystem and you come back out
42:1742분 17초the harnesses that you can use now that are really powerful are the ones that I'm like oh-my Claude Code
42:2442분 24초I mean, some of the harnesses, I mean, the skill sets, I mean, the skill sets, I don't think of them as harnesses
42:3442분 34초It's a set of skills, not a harness I don't think you can call it a system, unless you're saying it's not valuable but I don't think you can call it a system
42:4242분 42초It's a set of skills and agents, yes I think it's a harness because you're thinking about and creating those state machines that can make it long-running, and
42:5042분 50초then inside those state machines, how do you control the state graphs, how do you transition from this state to that state
42:5842분 58초what protocols do you use, and all that kind of stuff And then you can make it a closed loop, and you can set termination conditions, and things like that, but
43:0743분 7초I think OMC is a little bit of an alternative to what I've seen out there
43:1443분 14초And with the emergence of some of these harnesses, I think it's really kind of a democratization, or
43:2243분 22초should I say democratization of development
43:4843분 48초And again, I think the learning curve is really lower than it used to be, like you said, to the point where you're talking about a zero
43:5743분 57초learning curve So I'm kind of wondering if you're saying that because you've
44:0544분 5초really gotten it to a certain level Line: It's a little bit of a marketing thing So if you want to write
챕터 17: OMC와 클로드 코드의 사용자 경험
44:1344분 13초really deep, of course, if you understand it and write it, you can almost have a lot of width, but that's almost the whole point of zero ink
44:2344분 23초I don't have to memorize the skill names Claude, so some people really don't like this, but yeah, OMC
44:2944분 29초and OMX basically just overwrite the Claude MD or the Agent MD in the global or in the project and just start there
44:3744분 37초Our presets just put all the orchestration rules in there It doesn't have anything in there except the orchestration rules
44:4444분 44초And then you don't have to worry about omcOMX where you put all the project details, it's all in that note
44:5244분 52초pad and the project memory MCPs I have a separate place to store that structured stuff You're almost forced to use it
45:0045분I don't understand why this is the case for power users, and it can be a little annoying It feels like I don't use everything I've customized and
45:0745분 7초waste it without using it, so I tell those people that if they don't like it, don't use this and just customize it yourself
45:1545분 15초Usually if that's the case, then I don't think they're really the target audience, and I think we can move forward
45:2345분 23초with migration tools or something like that I mean, we have a wiki in OMC that we've just recently integrated, so I think we can provide tools like that to move
45:3145분 31초things over to the wiki or something like that, but anyway for people who are new to it it's not like Claude MD is going to be that overnight
45:3845분 38초If I don't have anything customized anyway, then that Claude MD will just have a skill map that basically says how to orchestrate which skill in
45:4545분 45초which context and which agent to infork and how to orchestrate it So it's like a skill map so it's a learning curve for us
45:5245분 52초And then we have keyword detectors And then there's keyword detectors, for example, just do it for me, so the autopilot skill just becomes
46:0046분this mock on the screen, or this is sometimes a lot of force initiatives, but there's nothing like this for people who don't know anything and are using it as a real vibe
46:0946분 9초If you just use it roughly, the best UX is when you just use it roughly OMC is a little bit like that, although OMX is tuned in a different direction
46:1646분 16초It's just You can think of Claude Code as a little bit like a studio, but it's a
46:2446분 24초studio and it's unfurnished No furniture, no cooking utensils, no nothing It's just a tin can studio with no options
46:3146분 31초But I think the idea is that now we just give you that full option all at
46:3846분 38초once and OMC just puts the full option in there Probably in terms of the Claude Code plugin
46:4446분 44초the more I use it, the more I use it, the more I feel like it's really powerful
46:5146분 51초and like you were saying earlier, you know, for that web web builder, oh-my OpenCode is so great right now
47:3147분 31초Yeah, so it's funny because it's less cognitive load, so it didn't
47:3847분 38초make sense for people to just turn on their original five sessions and just code I think in the early versions where there was no cursor
47:4747분 47초agent, it was just one file that I was working on and it was just kind of like I'm not going to switch to a chrome tab from there, but
47:5547분 55초obviously now it's just because of that harness, it's actually a budget thing where if you press it once, it's going to go back two and a half minutes
48:0348분 3초so that's why I have five or six or seven sessions open now It's actually a little bit of an expert or a little bit of a challenge to
48:1348분 13초manage that, but it's really just a little bit crazy to manage that
48:1948분 19초And it made me very, very curious about the point at which I decided to build
48:2748분 27초some of these harnesses And the common sense is, how could there be a harness like this when there were already great tools
48:3548분 35초like Claude Code, and there's a great company like Anthropic, and how could there be a
48:4248분 42초harness like this that surpasses it, and I was a little bit curious about that Now this is a very common objection that
48:5048분 50초I get a lot, so one is that it's a feature that's coming out in Claude Code anyway, so
48:5648분 56초it's going to come out, and I think that's actually half-true because people like us
49:0349분 3초are building it, and if people didn't like it, Anthropic wouldn't have put it in, and the second is that
49:1149분 11초Anthropic could do the same thing but they have different interests It's like this So right now, if you buy Hyundai's best-selling car, the
49:2049분 20초Avante, you can get up to 200 kilometers But if you put three turbos on it, put premium
49:2949분 29초oil in it, put nitro in it you can go 300 kilometers, right Put good tires on
49:3649분 36초it, but the manufacturer doesn't sell that shit Of course, but now people whose goal is, "I need to go fast,"
49:4449분 44초there's no reason not to There's just another market for it So it's a very asymmetrical demand, but from
49:5249분 52초the point of view of the coding agent here, it's actually more of a demand here There's more demand for tight tuning
50:0150분 1초And the reason why I don't think Anthropic is going to make a harness like this is because if you look at the
50:1050분 10초Claude Code source analysis articles, they've got a lot of tokens somehow So tuning, so think of me as a model provider
50:1750분 17초It's a coding tool that model providers make It's in the model provider's interest But if it's made by people who are
50:2650분 26초not in the model provider's interest, they can do much more extreme tuning The model provider hates it, but
50:3450분 34초there's nothing more limiting to that provider than having a bunch of file lead tool calls going on in parallel
50:4150분 41초Those are really tough requests I'm sure the lender engineers there have a hard time But it's unfortunate that they're struggling with
챕터 18: 튜닝과 성능 최적화에 대한 논의
50:4950분 49초it, but it's unavoidable, and we want to tune something and use it That's the concept So we don't have a vested interest
50:5750분 57초in the model provider, so we can just tune it from the concept of performance deliverability and
51:0551분 5초then just burning more tokens, burning more money but lowering people's cognitive load I think that's why people are kind of excited about it
51:1451분 14초I mean, I've been around for a while, and when the idea of the Ralph Loop came up, Claude Code also released it as an official plugin
51:2351분 23초But it's like, this is really beyond a little bit of mild flavor, it's like, it's just a little bit of a fierce flavor, a little
51:3051분 30초bit of this If you look at the officially supported Ralph loops That's not Ralph Now Jeffrey Huntley, the guy who's doing the Ralph Tone, the day
51:4051분 40초before I did that Ralph Tone, I was flying out of San Francisco and I made two round trips through Incheon Airport that day, and now
51:4751분 47초I went to pick him up in the morning And the host, Mr. Do-yoon, and the host, Mr Do-yoon, he was laughing that that's not Ralph
51:5551분 55초Didn't you say that you stayed at Mr. Ye Chan's house That's right Yes, he stayed at my house
52:0352분 3초It's so crazy that he came to Korea and that he stayed at your house since he came to Korea
52:1052분 10초I've been in San Francisco in the meantime anyway, and it's an Airbnb, you know So from that perspective a little bit, I'm kind of thinking that maybe real
챕터 19: OMC와 OMx의 활용 및 CLI 컨트롤 방식
52:2052분 20초people are a little bit into this flavor of poltuning and they're kind of really interested in harnesses like OMC
52:2852분 28초and OMX right now Steroids. Steroids Yeah, it's a little bit, people
52:3552분 35초who have used it, they just love the flavor of it. Oh, and one more thing I was asking Yeonkyu, it seems
52:4352분 43초like everybody's kind of moving towards this OpenClaw and Hermes agent and just kind of moving
52:5452분 54초towards this Claude Code or Codex with the CLI and just being able to control it That's right
53:0053분The first user of the CLI is actually becoming the agent So is that what you're doing right now with the
53:1053분 10초OpenClaw gazetteer just kind of controlling the CLI on its own It's kind of like that I have control of the CI, but I've been developing a little bit of
53:1953분 19초the reviews and utilities and stuff like that Nowadays, they develop and write their own stuff if they need to and yeah, that doesn't work well
53:2653분 26초but honestly, that doesn't work well, so sometimes I clean up that slop, but anyway, the CLI, so there's probably a lot more tokens that Gadget uses
53:3653분 36초as a CLI than I use as a CLI That's probably the way it is What are we humans supposed to do
53:4553분 45초If you give me money, I'll give you tokens The irony of that is I have so much to do right now I shouldn't have anything to do, but obviously, if I think about it, I should
53:5353분 53초be playing and eating right now and I'm so frustrated with myself I thought that if I work so
54:0054분hard on AI, I can play and eat comfortably, but it's sad how this is just more and more work to do Oh
54:0754분 7초So, since we're running a little bit late again, I thought I'd just show you how to use that OMX or OMC
54:1554분 15초a little bit and then we'll be done I have to work anyway, so I'm just going to get some issues out of the way
챕터 20: ️ OMx를 활용한 작업 흐름과 인터뷰 스킬
54:2454분 24초Yeah, yeah, yeah, yeah, I think this is going to get a little bit of a reaction
54:3354분 33초I've been pushing OMX a little bit lately so I'll show you OMX with it I do all my development on the iPad I almost don't have a development environment on the iPad
54:4254분 42초but I almost connect to it to develop, so let's take a look at the issue ticket status right now
54:5054분 50초This is just the Ubuntu CLI server server connection screen
54:5954분 59초I'm going to close 8 issues in OMC OMX
55:1055분 10초I know I'm not supposed to do this, but
55:2555분 25초What day is it Today is April 8th So we've got Codex, and then we've got this thing down here called OMX
55:3355분 33초And this one, this one, this one is actually not a Codex feature These are all tmux screens I'm just splitting everything up into tmux pane It automatically splits the tmux pane
55:4355분 43초This is this is this is this is this is this is this is a new feature and I have to demo it, so I left the ah pass on, so I'm out
55:4955분 49초of here fast, so let's see this, so we're going to do a standard layout table
55:5755분 57초We do what's called a deep interview It's where you keep asking questions until you're sure of something But I'm probably not going to ask you that many questions because we're just getting this off the table
56:1756분 17초I'll just say this much This is what happens sometimes when I'm using a proxy for something
56:2756분 27초You'll just have to wait That It's turned into a four-walking and
56:3456분 34초if you look at it now, it's got an interview or something down here Now my main tanner friend is cropping this a little bit too much
56:4156분 41초I don't know if it makes sense for the CLI to show this a little bit prettier, but people seem to like it
56:5056분 50초If you look at this, you've invoked a skill now called DeInterview When you invoke a skill, you get a keyword detector hook here
56:5756분 57초So the reason why I'm doing this now with OMX is because Claude, in this review, it's very silent and it's showing
57:0557분 5초up, but it's a recent review, like Codex So this is surprisingly recent It's very recent, it's still experiential
57:1257분 12초Experience, this tmux is scrolling a little bit weird but if you look here, the user prompt summit detected workflow keyword is detected
57:2157분 21초Now that the keyword is detected, it automatically initializes the deep interview state, so it's going to say HD, interview colon intent first, and then it's
57:3057분 30초just going to have a simple guidance front So that's the beginning of the simple steering, and now here, before we do the interview
57:4057분 40초what was I saying earlier I kept saying cognitive load So at the end of the day, the
57:4657분 46초reason we're using this is to reduce the cognitive load that I have to do to accomplish something That's right
57:5357분 53초So our workflow is almost like, we do the interview first Until there's no ambiguity
58:0158분 1초But it's kind of annoying if you're interviewing me and you're telling me something that I can find out by looking up the code So the interviewing skill itself is kind of like a brown field tease at first
58:1058분 10초so you find out as much as you can about what's already there and then you start to interview You're just kind of looking for
58:1858분 18초something right now Good Yeah, so I'll do a state walk like this, and
58:2758분 27초then I'll do a note pad walk, and then I'll do a note pad walk, and then I'll do a state walk, and then I'll do a state walk, and then I'll do a state walk, and then I'll
58:3658분 36초do a state walk, and then I'll do a state walk, and then I'll do a state walk, and then I'll do a state walk So that's something that you can pull out and continue or use later on
58:4658분 46초and for things like that notepad, just to see what you were originally doing when it was compressed, it's like you're still taking notes in a notebook, so you open a new session and
58:5458분 54초that notepad lightwork becomes an injection and you start it It says there are three open
59:0159분 1초labeled GitHub issues in the same folder I'm going to tell it to just open them up
59:0859분 8초because I need to do this quickly I'll just pull all the buggy ones, and then I'll use what's called a ral plan
59:1759분 17초If it's a little bit difficult, but this one takes about 30 minutes to run once The Jigga Plan, so it's a little bit like the Claude Ultra Plan
59:2559분 25초And this one, this one, this one, this one, this one, this one, this one, this one, this one, this one, this one, this one, this one, this one, this one, this one, this one, this one, this one, this one, this one, this one, this one, this one, this one
59:3259분 32초One for it, one against it, and then in the middle of that is now the one who's in favor of it, and then the one who's in favor of it, and only when all three of them are happy with the answer do we do the influencing
59:4159분 41초So that's the pre-mortem that I always emphasize So before you actually implement it, you want to make sure that you've debated all of the possible paths that could go wrong
59:5059분 50초before you actually implement it You're asking me this again
챕터 21: 버그 수정과 워크플로우의 위험성
1:00:081시간 8초It's a bug, it's a bug, it's a bug, it's a bug, it's a bug I was really stuck on that terminology that you mentioned
1:00:171시간 17초Something about the old ways of doing things you keep building and fixing Yeah, that's right That's what I didn't like
1:00:251시간 25초That was my biggest complaint with OMO the whole time I mean, things like home trading workflows and stuff like that, you know, it's really bad when you do that
1:00:331시간 33초There are certain kinds of things that are very dangerous to build and then tinker with and fix Think about building a spaceship
1:00:411시간 41초Unless it's extreme, you're building hospital software or something like that, and you're tinkering with it You know, software where every time you fix it, somebody dies or you lose $100
1:00:501시간 50초million of my money There are so many people who say, "You shouldn't vibe code things like that," and I don't agree with that
1:00:591시간 59초So let's make it as free as possible, so I have to make them ask me questions again that I haven't even considered So I've been looking for ways to do that, and
1:01:081시간 1분 8초now I've found one of my favorite people, Jagyu who created ouroboros, and I can introduce him to you if you want to interview me Please introduce me
1:01:171시간 1분 17초Jagyu, you made Geppetto Because I think I heard you talk a little
1:01:261시간 1분 26초bit in there about how both oh-my OpenCode and oh-my Claude Code
1:01:331시간 1분 33초were a little bit influenced by that repository I don't think it's OMO We are We're in the repo I brought a lot of these interview skills with me
1:01:411시간 1분 41초And then after that, we've got La Plan but actually, I mean, the agreed upon thing that I just mentioned
1:01:511시간 1분 51초I'm just going to do a procedure with a ralplan I think it was easy to take it and just use it
1:02:001시간 2분because all the commands that I needed to use I could just use that and everything would be done
1:02:121시간 2분 12초I'm not supposed to do this in interviews but I usually just go along with it until he tells me that I've passed the interview
챕터 22: ️ 인터뷰와 플래닝의 중요성
1:02:191시간 2분 19초I also have that Embiguity stress hold really low So I can set the stage for that as well I don't necessarily want to be interviewing for hours on
1:02:261시간 2분 26초end for a simple doxing or something like that, so there's another thing where I can set how deep I want to go There are also skill guidelines
1:02:351시간 2분 35초like flags or just natural language I think it would be great to utilize that, and if you just have something in your mind, you can just tell her
1:02:431시간 2분 43초and she'll probably have something Straight from the Deep Interview Ultra Plan is really
1:02:511시간 2분 51초I think it's probably a lot more efficient than the Ultra Plan But it's a lot of words Is it worth it, but I think it's worth it
1:03:001시간 3분Because there's a huge difference between what I did after the interview and what I didn't do So the interviews are like a series of multiple choice questions
1:03:081시간 3분 8초Especially in the OMC, the deep just ask user question tool where you can just keep clicking away with the multiple choice questions
1:03:161시간 3분 16초And then if I don't turn it around, sometimes there's a contradiction in my interview Because sometimes I've interviewed someone and they've said they're going
1:03:241시간 3분 24초to implement something that they can't implement at all, or they've given me very conflicting answers The human brain is so geographically malleable, and
1:03:341시간 3분 34초the human brain is the most cognitively malleable, so that's why Ralphlen nips it in the bud Because the planner rolls it up once, and then the planner
1:03:431시간 3분 43초basically follows the specs that I've laid out But now there's a kid who keeps disagreeing with me about that spec because it's wrong because it's so-and-so, and
1:03:531시간 3분 53초he's right, and he's right, and he's right so let's come to an agreement and then there's an agent who agrees with us and that's now our La Plan
1:04:011시간 4분 1초And it can take a long time because those three agents keep doing something until they come to an agreement Especially if it's complicated, then what's really nice about this Rai plan is that
1:04:091시간 4분 9초it's a plan for how we're going to assign teammates or agents later on in the process
1:04:181시간 4분 18초It's like a work plan So It's like, you know, it's a really tight pre-mortem
1:04:251시간 4분 25초So I'm like, you know, it's like this I sit down for interviews and I'm like, "Okay, I'm going to write the important stuff, I'm going to write the important stuff
1:04:331시간 4분 33초Especially for features, I'll sit down and interview for like 20 minutes straight I spend 10, 20 minutes just answering questions I just sit there and
1:04:411시간 4분 41초then La Plan is a handoff It's like 30 to 40 minutes, and then I just kind of skim through the plan and then I just kind of go into Ralph's team mode or
1:04:491시간 4분 49초Ralph's mode and just run it all the way through until that spec is implemented Until that specification is implemented, and then at the end, I just try it out as a
1:04:591시간 4분 59초user, and if you go through that process, I think it's actually a clean shopping experience I mean, those are really just the three steps that you're talking about
1:05:081시간 5분 8초But those three steps are actually a workflow that was a little bit really difficult even with a ten or
1:05:181시간 5분 18초twenty person organization before, and I think it's really kind of amazing that you can do
1:05:251시간 5분 25초it in those three steps by yourself But what I think actually differentiates this
1:05:311시간 5분 31초a little bit from, you know, basic Claude Code or especially agents like cursors, I mean, there's a lot of tools
1:05:391시간 5분 39초out there where the line between planning and execution is still not clear I've written that vanilla Claude Code forces you to plan and
1:05:491시간 5분 49초Codex forces you to plan, but I don't think that's true So I'm an asshole, so I'm
1:05:561시간 5분 56초too open, so I've built up a lot of resentment towards a lot of different people and basically started to assume that users are all stupid
1:06:051시간 6분 5초I'm stupid too, so there's basically a lot of things that I haven't considered and I'm going to create a segment that's going to
1:06:131시간 6분 13초give me just the right cognitive load by continuing that It's like 10, 20 minutes, and then once I'm done with
1:06:201시간 6분 20초that load, then the handoff should be clean So that's the handoff, and then I can go do something
1:06:281시간 6분 28초else for the next couple hours That's right I think that's the key for me I'm in the middle of it and I'm like, "Oh, this is something I didn't consider
1:06:361시간 6분 36초If I have to fix it again, if I have to keep prompting, I'm just going to throw that session away and do a new one
1:06:431시간 6분 43초So this is one of the things that I see people doing wrong with OMX and I see people doing wrong with interviews, is they'll give you a bunch of interview answers
1:06:501시간 6분 50초because they don't want to bother answering the interview, and then they'll see it implemented and they don't like it, and they'll throw a prompt in the middle of it, and then it's like, "Oh, I didn't think of that
1:06:581시간 6분 58초It completely ruins the project If you're going to do that, you might as well just tear this thing down and use it as a Brannon Fields joke and get a new interview
1:07:071시간 7분 7초I do that a lot And then if I feel like it, I'll probably put up a critique because the planner's made it now
1:07:141시간 7분 14초And then I'll show you one last thing that's just cool That's people's favorite part It's kind of the
1:07:231시간 7분 23초whole point of this OMC OMX, the primitives concept I think that's the keyword Primitem is the keyword That's what I'm pushing
챕터 23: 프리모템과 프로젝트 관리의 핵심
1:07:311시간 7분 31초But I don't see a lot of people doing this Because if you ask me, is it realistic to have
1:07:391시간 7분 39초a project that needs this much pre-mortem or do you really need this much pre-mortem for light development purposes, I honestly don't think so
1:07:481시간 7분 48초So if I want to make a website that sells health supplements, for example do I need this many pre-mortems or not
1:07:551시간 7분 55초I think I can just build it and fix it, but what I've been trying to do with OMO, I mean, everything I've been trying to do with OMO or whatever I've been trying to
1:08:041시간 8분 4초do growing up, it's almost all quantitative trading stuff There are a lot of details that I don't know that I
1:08:111시간 8분 11초didn't think of, and I want to write it down and start, but that's also very difficult, and then there are a lot of parts
1:08:191시간 8분 19초that almost have to deal with formulas, so if one logic is flipped, everything behind it is flipped, and I think
1:08:271시간 8분 27초that's why I thought about primitives so much I think that's a really important point Really Yeah, I just closed all the Planner Architects here
1:08:371시간 8분 37초And then I have four Teamwork Spain right now This one, this one, this one this one Isn't that the whole point of OMX This is the whole point of OMX
1:08:451시간 8분 45초It's team mode So they're on their own Suddenly this tickles my fancy That's right It's just kind of like, I'm in a good mood again, so
1:08:521시간 8분 52초I put this up and it's kind of like, I like that kind of vibe I like live, but it's actually efficient in my opinion
1:09:001시간 9분The key to this team mode is that you don't just have four of these up and they communicate with each other and do their own thing and that's it
챕터 24: 팀모드의 핵심과 워크 트리 구조
1:09:081시간 9분 8초Each one of these workers has a separate work tree And underneath that work tree, there's another work tree
1:09:141시간 9분 14초And then how do I do this systematically, I'm looking at everything I'm looking at everything, and if there's a file defect, I'm
1:09:221시간 9분 22초going to commit it systematically, and then I'm going to fast-forward that commit back to the leader branch
1:09:301시간 9분 30초But sometimes fast-forwarding can get conflicts And when it does, I'll give the leader a nudge to say, "Hey this is incomplete, fix the incomplete Guys
챕터 25: 병합 문제와 팀모드의 해결책
1:09:381시간 9분 38초The reason why we need to do this is basically the problem with using sub-agents so heavily is that when you
1:09:451시간 9분 45초have to go back and merge everything you have a lot of problems So especially with that real world thing, it would be
1:09:541시간 9분 54초nice to have a really clean division of the scope but there's a lot of things that can't be ideally divided I have a lot of sub-agents running in parallel, and
1:10:011시간 10분 1초there are a lot of places where the scopes are forced to overlap If you don't want them to overlap, you can't do things in parallel, but then when you do, there's too many
1:10:101시간 10분 10초conflicts when you merge them Mm It's like if you picked a team of people and you just gave them to each of you and said, "You
1:10:181시간 10분 18초guys work on your own for a week and we'll see you in a week,"
1:10:221시간 10분 22초and then you try to merge them later That's very limiting Team mode prevents that Because we're all committing on a file-by-file basis and we're all communicating
1:10:321시간 10분 32초with each other right now on an action-by-action basis But why did I build this, I mean, I just kind of built this by
1:10:391시간 10분 39초accident, I mean, I think the whole point of team mode is to reduce the cost of this merge, so how do I enforce this collaboration protocol, so where
1:10:461시간 10분 46초is this coming from, how does it merge, what do we need to agree on, what are these protocols and I kept thinking about it, and then I realized that DAG
1:10:561시간 10분 56초is the only thing that doesn't do that And then I realized that Git worktree is a DAG, so I just use it to
챕터 26: 팀모드의 닫힌 루프와 효율성
1:11:051시간 11분 5초automatically cherry-pick, automatically fast-forward, and then when the leader branch is updated, it automatically rebases the workers again
1:11:141시간 11분 14초And it'll build back up from there If there's a rebase complication, then that's another command that tells the worker to fix the rebase
1:11:221시간 11분 22초complication, and then there's just these nudge commands, and then when you actually get the nudge, it's really contextual as to whether you as the leader should
1:11:301시간 11분 30초choose worker one or worker two I'll leave that to Eve So the whole workflow is a closed rope It's a closed
1:11:381시간 11분 38초rope, just a mathematically closed rope It's an algorithmically supported rope, but there's a part in the middle
1:11:461시간 11분 46초where you have to contextually steer it If you leave that steering to Eli to figure out where to take things and where to drop things when things get complicated, and then how to
1:11:541시간 11분 54초do this source tracking and where to go and what tasks to give, but
1:12:001시간 12분the whole workflow itself is a closed loop, you get a lot of silver token efficiency
1:12:071시간 12분 7초Because you don't have to have a bunch of useless context Because the workflow itself is a closed room
1:12:161시간 12분 16초all these telemetry is set If you look at it, there were messages just popping up in the reader pane
1:12:241시간 12분 24초I'm writing to myself, and then I'm writing to the OMX team API list task sand messages, and so on They're communicating with each other Inside of this telementry rule
1:12:331시간 12분 33초This is awesome This And then I've got a bunch of tasks right now that are popping up like this, Pandering 3
1:12:411시간 12분 41초Infinite Tour Compact Zero Failed Zero Let me see if this is still in the discord right now in Clawhip
1:12:501시간 12분 50초Hang on a second Did you ever introduce OMC and OMX like this
1:12:571시간 12분 57초in that slightly public way OMC OMX, I'll just kind of give a quick introduction This is so awesome
1:13:061시간 13분 6초It's really cool that you did a really great introduction You can pull it down and pull it up and it's fun
1:13:141시간 13분 14초Team mode is a kick And then the number of cued follow messages here right now I didn't put any messages in there I didn't touch anything It's just nudging in on its own
챕터 27: 팀워크와 자동화된 협업 시스템
1:13:221시간 13분 22초They're manipulating the tmux with their tmux sand key So you hear a lot of people talking about cmux and tmux
1:13:301시간 13분 30초and all these different agents that they're putting up and saying, "Oh, what should I do That control is automated So the truth is that that control is hard and
1:13:401시간 13분 40초you can't really do it That control pane is all automated This is this is this is this is team mode
1:13:481시간 13분 48초So I don't think I can run a bunch of subagents and say that's a team of agents Basically, I think a team is a team when you communicate in the middle of what
1:13:571시간 13분 57초you're doing It's not a team if you don't communicate at the end We're just taking that protocol and applying it here It's nothing new
1:14:051시간 14분 5초It's the original work tool, it's the original DAG it's the original collaboration methodology How do you just tweak it a little bit to let LLM do the steering
1:14:151시간 14분 15초yeah, and then at the end of the day, you know, now for things like workerforces, you know, you do identity-paid root queries or something like that
1:14:241시간 14분 24초So this is what they're all talking about right now on the teleprompter And then we're probably starting to see the work
1:14:321시간 14분 32초commits come up here now The last thing I want to show you is, let's
1:14:401시간 14분 40초see, here's our disco room I've got OMC DEV on Clawhip and I'm just spinning it up right now
1:14:471시간 14분 47초Fix issue sweep 0408 auto checkpoint walker 3 mudge walker 3 mudge walker 3 like this, so the auto mudge is holding everything
1:14:531시간 14분 53초It's on the leader branch, it's in the room, yeah, this is the session that I'm running, so
1:15:001시간 15분it's not nudging the gauge right now All the things that are going on to make sure that all the messages are coming over there
1:15:101시간 15분 10초Yeah Because that way, I'm doing my work and he's doing his work and we're not out of context He's going to read this message later, so
1:15:171시간 15분 17초I'm going to tag him once, and then he's like, "Oh, you did this," and then I'm like, "Oh, I'm going to do another issue
1:15:241시간 15분 24초Or I'm doing duplicate work and wasting tokens, so I'm still running around So now the team is giving me nudges like, "Hey, unblock this
1:15:331시간 15분 33초because you're not making progress," so it's just kind of an honor protocol So, you know, there's all these management books about
1:15:411시간 15분 41초how a company should be run, or just senior managers talking about how a tech company should be run
1:15:501시간 15분 50초I think it's really useful and fun to just borrow those concepts one by one
1:15:571시간 15분 57초You pretty much built this on your own, didn't you Yeah, it's kind of weird that I built this on my own
1:16:061시간 16분 6초I do have a maintainer friend who's been helping me with the team runtime and especially the UX side of things But the first time I cut the Coco runtime, I actually cut
1:16:151시간 16분 15초it from the first time I did this OMX, and he cut it a little bit later, so now it's a little bit later
1:16:221시간 16분 22초and now it's a little bit cleaner for someone who doesn't know about hardening or team mode, so it's full proof And that's really important from a
1:16:301시간 16분 30초product point of view because now I know, I know how team mode works and I know how it doesn't work
1:16:381시간 16분 38초But I have a main tainer friend who's been polishing it a little bit from a UX perspective so that it's a little bit usable for people who don't know that
1:16:451시간 16분 45초I think it's really too oh-my OpenCode shooting and another very real, a little
1:16:531시간 16분 53초bit of color separation I think there's definitely a little bit of a color difference between the two, and then
1:17:021시간 17분 2초there's this We just had a message go to auto It's like, "Hey, Walker Three is now out of business and not working, so what do you do about it?" It's just giving
1:17:111시간 17분 11초you a little bit of a nudge The steering, for example, in the received loop By the way, aren't you doing OMOcon again on
1:17:211시간 17분 21초April 25th with Yeonkyu, Jinhyung, and Yeechan That's right Yes, I hope you'll come to OMOCon as well
챕터 28: OMC 행사와 글로벌 AI 인재의 특징
1:17:291시간 17분 29초It's actually really oversubscribed right now, but we're going to try We're going to do it, so I'm really excited
1:17:361시간 17분 36초about that, but unfortunately, I'm not in Korea again so if you want to join us, you can
1:17:421시간 17분 42초do it online, and I'll put this link up on the screen but isn't it already closed again It's not closed
1:17:501시간 17분 50초We would like to invite everyone to register, but we are prioritizing only those who have already contributed something
1:18:001시간 18분to OMO or OMC OMX or have a high level of involvement I think we're going to have to ask for a little
1:18:091시간 18분 9초bit of understanding that we can only bring in a few people who are interested or really need to hear it
1:18:161시간 18분 16초I think all the big name developers are coming It's not finalized It's still I think it's one of those events that if you're
1:18:261시간 18분 26초actually in Korea, you should definitely go to and it seems like the three of you are doing a lot of events these days to really get together
1:18:351시간 18분 35초Yeah, that's right We've been doing a lot of things and we've been doing a lot of global things
1:18:431시간 18분 43초I'm really looking forward to it and I think you three have a little bit in common If you look at the three of you, I've interviewed all three of you
1:18:521시간 18분 52초Yeah, I think there are some things that are a little bit different I don't know how I thought about this, but when we talked
1:19:001시간 19분about these points it seemed like the three of you had a little bit in common Yeah, he's also doing a shutdown
1:19:081시간 19분 8초I think I'll just see the auto-checkpoints shut down and then I'll be done Where did you get that idea from
1:19:171시간 19분 17초I don't know if Jinhyung or Yeonkyu or me Uh, first of all, I think a little
1:19:251시간 19분 25초bit in general, people have their own hurdles I guess what I'm trying to say is that I feel a little bit like when I found
1:19:311시간 19분 31초out about Claude Code, I feel like it was a little bit like those people in Attack on Titan realized that there's
1:19:391시간 19분 39초a whole other world beyond that wall, or it was an event for me where the silver blind opened their eyes
1:19:481시간 19분 48초I mean, we always have a very clear cut limit of what we can do, but I should say that you guys are a little bit blind to that line, or I should say that you guys are a little bit
1:19:571시간 19분 57초blind to that line, or I should say that people of this caliber people of this specification, people of this caliber would normally think, ah
1:20:061시간 20분 6초I can't do this, but you guys are a little bit blind to that line, but I think that feeling was a little bit common to all three of them
1:20:141시간 20분 14초So, I was thinking that there was a little bit of that in common between the three of
1:20:211시간 20분 21초you, that you were a little bit deeply immersed in it and a little bit
1:20:301시간 20분 30초driven to complete a project that people thought would be a little bit impossible
1:20:381시간 20분 38초Yeah Yeah We're kind of weird people I think one of the things that I'm kind of rooting for right now, which I was a little bit wary of talking
챕터 29: 세 명의 인물과 그들의 독특한 배경
1:20:471시간 20분 47초about, is that the three of you have another thing in common, you're all high school graduates Yeah But, you know
1:21:051시간 21분 5초No, no, no, no, I think it's a little bit of a meme No, no, no, it's a little bit of a meme It's a meme that we have a lot of fun with
1:21:141시간 21분 14초I'm one of those people who thinks that times have changed and I'm very much
1:21:201시간 21분 20초cheering for you guys because I feel like you guys are kind of pushing Korea's AI in this direction a little bit now, and I feel
1:21:291시간 21분 29초like you guys have some influence and you're kind of steering the ship And the three of you are
1:21:361시간 21분 36초a little bit like this on Jinhyung's podcast so I asked Yeonkyu, too I asked you if you went to study abroad or if
1:21:441시간 21분 44초you were from Yeongyu when you were younger, but it's not like that at all But you said that you
1:21:511시간 21분 51초just self-taught yourself in Korea because you had a purpose to learn a little bit so wow, that's a little different
1:22:001시간 22분But also, Yeechan, you are also like that, and a little bit like that, the three of you have a little bit in common, and I think that
1:22:071시간 22분 7초I can be an important example of some talented people who have to go global in the AI era in
1:22:151시간 22분 15초the global era, so I am supporting you very much Okay, thank you
1:22:211시간 22분 21초Yeah so I think that was a little bit of the feeling that I had with the three of you is
1:22:311시간 22분 31초that you don't have that huddle threshold that most people have So I think it's hard for me to come up with something like
1:22:391시간 22분 39초this if I don't have that common feeling of, yeah I think that's part of it This is a time when it's really important to do unlearning, and
챕터 30: AI와 한국의 미래에 대한 논의
1:22:461시간 22분 46초we're not people who have been doing things in
1:22:531시간 22분 53초such a structured way to learn things in the first place, so yeah, I think there's a little bit more freedom in that
1:23:011시간 23분 1초So I think that's why I realized that not only me but also Mr. Noh felt the same way
1:23:091시간 23분 9초So I think he was really impressed with the tribute session in particular And you just described the people
1:23:151시간 23분 15초there as fresh, young, and fresh and I think that's what I felt very
1:23:221시간 23분 22초strongly that day, that their actions will have a lot of impact on the
1:23:321시간 23분 32초future development of the real Korean AI But then all of a sudden something like this happened again
1:23:411시간 23분 41초and it was very global Yeah, that's right And then I realized that
1:23:481시간 23분 48초there were people who said that they were going to do something
1:23:551시간 23분 55초So I think you're probably hearing a lot of things again because you're so famous
1:24:041시간 24분 4초again, but I think that's just another noise that can't be helped, and I
1:24:111시간 24분 11초think your personality won't be affected much again That's right
챕터 31: 툴 개발과 촬영의 의미
1:24:181시간 24분 18초We just laugh about it Yeah, but really
1:24:241시간 24분 24초I've been really interested in this tool and I've been testing it a lot and I've been in the shoes of someone like that
1:24:311시간 24분 31초and when the developer himself explains it to me like this it really makes me think that if people who don't know about it yet start to get interested in it, they're going to be able
1:24:411시간 24분 41초to produce a lot more amazing things, so I think that's why today was so meaningful
1:24:501시간 24분 50초It was fun for me too I've been working a lot Yeah, and finally, you've been a
1:24:571시간 24분 57초little bit busy lately Can you tell us a little bit about
1:25:051시간 25분 5초what you're doing this year or in the future, even if it's just briefly, and for those who are supporting you and for those who are using OMC
1:25:141시간 25분 14초and OMX, yes I actually only have a plan for this week or so
1:25:211시간 25분 21초Anthropic here doesn't have a long-term plan, and there's no long-term plan there, but I don't think there's actually a reason to
1:25:281시간 25분 28초have one, and I've lived without it before this, and I just have a plan for this week I have a plan to do OMOcon on April 25th
1:25:361시간 25분 36초So other than that, there's not much I'll probably get caught Continuing That's so cool
1:25:441시간 25분 44초One week I don't recommend planning for more than a week these days because I've seen too many
1:25:521시간 25분 52초times that planning for more than a week is pointless Yeah ah really but a lot of people
챕터 32: 콘텐츠와 향후 기대
1:25:591시간 25분 59초are really going to be following Jinhyung and Yeechan and Yeonkyu a lot now and seeing what they're doing
1:26:071시간 26분 7초Yeah You shouldn't follow us either because we're human beings who don't know how we're gonna feel tomorrow and where we're
1:26:141시간 26분 14초gonna go It's kind of crazy I'm so excited
1:26:241시간 26분 24초OMC OMX is going to be huge Yeah, so I'm hoping that even if it's just a little bit, I'm hoping that we'll make a little bit of
1:26:331시간 26분 33초money from this video If that happens, I'm so grateful Because Jinhyung, you came out and you have about 80,000 views now
1:26:421시간 26분 42초Oh, it's really good Yeonkyu has about 40,000 views But Jinhyung came out three or four times, and it's almost over 100,000 Oh, cumulatively
1:26:501시간 26분 50초Yeah, I think this content is going to be tough I see Why don't we try for 100,000 with one video
1:26:581시간 26분 58초Yeah I think we can do that Okay, I know you're busy today, but thank you so much for joining us again and I'll try to get it edited and uploaded
1:27:071시간 27분 7초Thank you very much Okay, that's all for now Thank you very much Okay, thank you very much
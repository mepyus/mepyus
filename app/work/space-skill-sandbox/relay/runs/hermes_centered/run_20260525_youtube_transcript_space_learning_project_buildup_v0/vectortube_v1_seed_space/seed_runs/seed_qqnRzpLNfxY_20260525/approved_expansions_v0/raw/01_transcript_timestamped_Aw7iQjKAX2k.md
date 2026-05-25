# Expansion transcript: Aw7iQjKAX2k

slot: rag_comparison
title_hint: GraphRAG vs. Traditional RAG
source_url: https://www.youtube.com/watch?v=Aw7iQjKAX2k
segment_count: 53
duration: 4:12

## Timestamped transcript

0:00 Imagine you're running a health care support line
0:02 where patients and providers are calling in with complex multi-step questions.
0:06 This is where GraphRAG comes in.
0:08 It helps map relationships, providing precise, personalized answer faster,
0:13 and this is critical where accuracy and speed matter.
0:17 Today, we're going to take a look at how GraphRAG helps in delivering higher accuracy
0:21 and more complete answers, easier development and maintenance and enhanced governance.
0:26 We'll go over what is GraphRAG and uncover the benefits of GraphRAG relative to traditional RAG in development,
0:34 Production,
0:36 and governance.
0:39 To understand GraphRAG, let's first break down how Baseline graph works.
0:44 We start off with a private data set,
0:48 can be both structured and unstructured,
0:52 so this is our traditional,
0:55 and we break them down into text chunks,
1:02 and we store those embeddings in a vector database.
1:08 Then when we want to query,
1:14 we use our vector database to extract the context, and then we send that context to our LLM,
1:21 and then it provides the answer.
1:23 We all know how tradition RAG works.
1:25 Now GraphRAG builds on top of that.
1:32 We start off with leveraging same text chunks,
1:39 but on top of that, we're also extracting
1:41 entities and more relative information to be able to map out these information in a knowledge graph.
1:51 This way graph doesn't just retrieve isolated answers.
1:55 It connects relative information which enhances the quality responses and added accuracy and insight.
2:02 Let's consider an example to demonstrate the capabilities of GraphRAG.
2:06 Suppose we have a sentence like this, "an immunologists discussed virus
2:11 response strategies with the CEO of a health care company."
2:14 Traditional text analysis might have detected immunologist and CEO as named entities.
2:21 However, GraphRAG goes further by identifying and mapping the relationships between these entities,
2:29 and this provides a deeper context and insight into their interaction.
2:34 So GraphRAG recognizes that the immunologist is deeply connected to immunology and the medical research.
2:41 Whereas the CEO has more of an indirect yet related connection through her leadership at the health care company,
2:47 This analysis goes beyond just simply noting co-occurrences.
2:52 The LLM quantifies the strength and nature of these relationships,
2:56 enabling the construction of weighted graphs that reveal insightful patterns.
3:01 Transforming data into knowledge graph creates a network of connected and linked entities,
3:07 and the linked multilayered knowledge graph then supports a wide range of applications,
3:12 and generating targeted questions to crafting rich and contextually relevant summaries,
3:17 ultimately providing a depth of insights that traditional RAG cannot achieve alone.
3:24 So going back to production, development and governance.
3:27 GraphRAG provides a higher accuracy,
3:33 and complete
3:37 answers a runtime.
3:40 As from a developer perspective, once you build up the graph, it's easier to maintain it.
3:46 Than it is with a traditional RAG.
3:48 And subsequently, once you're  querying it, you will get better explainability,
3:57 and traceability,
4:00 and access controls.
4:02 Thank you for watching.
4:03 And hope you like this video.
4:06 If you have any questions or comments, let me know below and don't forget to like and subscribe for more content like this.

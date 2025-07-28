from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

def rank_sections_and_snippets(sections, persona, job):
    query = persona + ". " + job
    query_emb = model.encode([query])[0]

    ranked_sections = []
    for sec in sections:
        sec_emb = model.encode([sec["text"]])[0]
        sim = cosine_similarity([query_emb], [sec_emb])[0][0]
        ranked_sections.append({
            "document": sec["document"],
            "page_number": sec["page"],
            "section_title": sec["title"],
            "text": sec["text"],
            "score": float(sim)
        })

    ranked_sections.sort(key=lambda x: x["score"], reverse=True)
    for i, sec in enumerate(ranked_sections):
        sec["importance_rank"] = i + 1

    top_sections = ranked_sections[:5]

    snippets = []
    for sec in top_sections:
        for para in sec["text"].split("\n"):
            if len(para.strip()) < 50:
                continue
            para_emb = model.encode([para])[0]
            score = cosine_similarity([query_emb], [para_emb])[0][0]
            snippets.append({
                "document": sec["document"],
                "refined_text": para.strip(),
                "page_number": sec["page_number"],
                "score": float(score)
            })

    snippets.sort(key=lambda x: x["score"], reverse=True)
    return top_sections, snippets[:5]

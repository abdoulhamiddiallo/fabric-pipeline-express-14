-- Contrôle dans WH_Inka après approbation : 4 lignes, 291 demandes et 2 380 visiteurs au total
SELECT circuit, COUNT(*) AS demandes, SUM(visitors) AS visiteurs FROM dbo.published_quota WHERE visit_date = '2026-11-02' GROUP BY circuit ORDER BY circuit;

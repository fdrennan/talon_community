from talon.voice import Context, Key

ctx = Context("dplyr")
#  this is a mapping for scrolling and other mouse utilities
#
# keymap = {

#     # scrolling
#     "scroll down": [Key("down")] * 30,
#     "scroll up": [Key("up")] * 30,
#     # NB home and end do not work in all apps
#     "(scroll way down | doomway)": Key("cmd-down"),
#     "(scroll way up | jeepway)": Key("cmd-up"),
#     "page up": [Key("pageup")],
#     "page down": [Key("pagedown")],
#     # searching
#     "(search | marco)": Key("cmd-f"),
#     "marneck": Key("cmd-g"),
#     "marpreev": Key("cmd-shift-g"),
#     "marthis": [Key("alt-right"), Key("shift-alt-left"), Key("cmd-f"), Key("enter")],
# }


keymap = {
    "import deplyr": ["library(deplyr)"],
    "import tidy": ["library(tidyverse)"],
    "tighty": ["tidy", Key("tab")],
    "deplyr package": ["dplyr::"],

    "deplyr table": ["tibble()", Key("left"), Key("enter")],
    "deplyr table inverse": ["tribble()", Key("left"), Key("enter")],

    "deplyr as tibble": ["as_tibble()", Key("left")],
    "deplyr is tibble": ["is_tibble()", Key("left")],
    "deplyr in frame": ["enframe()", Key("left")],

    "deplyr gather": ["gather(data = , key = , value = )"],
    "deplyr spread": ["spread(data = , key = , value = )"],

    "deplyr drop in": ["drop_na()", Key("left")],
    "deplyr fill": ["fill()", Key("left")],
    "deplyr replace": ["replace_na()", Key("left")],
    "deplyr complete": ["complete()", Key("left")],
    "deplyr expand": ["expand()", Key("left")],
    "deplyr separate": ["separate()", Key("left")],
    "deplyr separate rows": ["separate_rows()", Key("left")],
    "deplyr unite": ["unite()", Key("left")],


    "deplyr filter": ["filter()", Key("left"), Key("enter")],
    "deplyr mutate": ["mutate()", Key("left"), Key("enter")],
    "deplyr select": ["select()", Key("left"), Key("enter")],
    "deplyr summarize": ["summarise()", Key("left"), Key("enter")],
    "deplyr rename": ["rename()", Key("left"), Key("enter")],
    "deplyr group by": ["group_by()", Key("left"), Key("enter")],
    "deplyr transmute": ["transmute()", Key("left"), Key("enter")],

    "deplyr filter if": ["filter_if()", Key("left"), Key("enter")],
    "deplyr mutate if": ["mutate_if()", Key("left"), Key("enter")],
    "deplyr select if": ["select_if()", Key("left"), Key("enter")],
    "deplyr summarize if": ["summarise_if()", Key("left"), Key("enter")],
    "deplyr rename if": ["rename_if()", Key("left"), Key("enter")],
    "deplyr group by if": ["group_by_if()", Key("left"), Key("enter")],
    "deplyr transmute if": ["transmute_if()", Key("left"), Key("enter")],

    "deplyr filter at": ["filter_at()", Key("left"), Key("enter")],
    "deplyr mutate at": ["mutate_at()", Key("left"), Key("enter")],
    "deplyr select at": ["select_at()", Key("left"), Key("enter")],
    "deplyr summarize at": ["summarise_at()", Key("left"), Key("enter")],
    "deplyr rename at": ["rename_at()", Key("left"), Key("enter")],
    "deplyr group at": ["group_by_at()", Key("left"), Key("enter")],
    "deplyr transmute at": ["transmute_at()", Key("left"), Key("enter")],

    "deplyr filter all": ["filter_all()", Key("left"), Key("enter")],
    "deplyr mutate all": ["mutate_all()", Key("left"), Key("enter")],
    "deplyr select all": ["select_all()", Key("left"), Key("enter")],
    "deplyr summarize all": ["summarise_all()", Key("left"), Key("enter")],
    "deplyr rename all": ["rename_all()", Key("left"), Key("enter")],
    "deplyr group by all": ["group_by_all()", Key("left"), Key("enter")],
    "deplyr transmute all": ["transmute_all()", Key("left"), Key("enter")],

    "deeplyr count": ["count()", Key("left")],
    "deeplyr on group": ["ungroup()"],
    "deplyr sample fraction": ["sample_frac()", Key("left")],
    "deplyr sample in": ["sample_n()", Key("left")],
    "deplyr slice": ["slice()", Key("left")],
    "deplyr top in": ["top_n()", Key("left")],

    "deplyr arrange": ["arrange()", Key("left")],
    "deplyr descending": ["desc()", Key("left")],

    "deplyr add row": ["add_row()", Key("left")],
    "deplyr add column": ["add_column will()", Key("left")],

    "deplyr pull": ["pull()", Key("left")],
    "deplyr everything": ["everything()"],
    "deplyr contains": ["contains()", Key("left")],
    "deplyr ends_with": ["ends_with()", Key("left")],
    "deplyr matches": ["matches()", Key("left")],
    "deplyr numb range": ["num_range()", Key("left")],
    "deplyr one of": ["one_of()", Key("left")],
    "deplyr starts with": ["starts_with()", Key("left")],
    "deplyr call names": [" %>% ", Key("enter"), "colnames"],

    "deplyr lag": ["lag()", Key("left")],
    "deplyr lead": ["lead()", Key("left")],
    "deplyr come all": ["cumall()", Key("left")],
    "deplyr come any": ["cumany()", Key("left")],
    "deplyr come max": ["cummax()", Key("left")],
    "deplyr come mean": ["cummean()", Key("left")],
    "deplyr come min": ["cummin()", Key("left")],
    "deplyr come prod": ["cumprod()", Key("left")],
    "deplyr come sum": ["cumsum()", Key("left")],
    "deplyr come dist": ["cume_dist()", Key("left")],
    "deplyr dense rank": ["dense_rank()", Key("left")],
    "deplyr min rank": ["min_rank()", Key("left")],
    "deplyr in tile": ["ntile()", Key("left")],
    "deplyr percent rank": ["percent_rank()", Key("left")],
    "deplyr row number": ["row_number()", Key("left")],
    "deplyr between": ["between()", Key("left")],
    "deplyr near": ["near()", Key("left")],

    "deplyr case": ["case_when()", Key("left"), Key("enter")],
    "deplyr coal": ["coalesce()", Key("left")],
    "deplyr if":      ["if_else()", Key("left")],
    "deplyr in if": ["na_if()", Key("left")],
    "deplyr pea max": ["pmax()", Key("left")],
    "deplyr pea min": ["pmin()", Key("left")],
    "deplyr recode": ["recode()", Key("left")],
    "deplyr recode factor": ["recode_factor()", Key("left")],

    "deplyr in": ["n()", Key("left")],
    "deplyr in distinct": ["n_distinct()", Key("left")],
    "deplyr mean": ["mean()", Key("left")],
    "deplyr median": ["median()", Key("left")],
    "deplyr sum": ["sum()", Key("left")],
    "deplyr first": ["first()", Key("left")],
    "deplyr last": ["last()", Key("left")],
    "deplyr inth": ["nth()", Key("left")],
    "deplyr men": ["min()", Key("left")],
    "deplyr max": ["max()", Key("left")],
    "deplyr quantile": ["quantile()", Key("left")],
    "deplyr eye queue are": ["IQR()", Key("left")],
    "deplyr mad": ["mad()", Key("left")],
    "deplyr standard deviation": ["sd()", Key("left")],
    "deplyr var": ["var()", Key("left")],
    "deplyr row to call": ["rownames_to_column()", Key("left")],
    "deplyr call to row": ["column_to_rownames()", Key("left")],
    "deplyr bind calls": ["bind_cols()", Key("left")],
    "deplyr bind rows": ["bind_rows()", Key("left")],
    "deplyr left join": ["left_join()", Key("left")],
    "deplyr right join": ["right_join()", Key("left")],
    "deplyr inner join": ["inner_join()", Key("left")],
    "deplyr full join": ["full_join()", Key("left")],
    "deplyr intersect": ["intersect()", Key("left")],
    "deplyr union": ["union()", Key("left")],
    "deplyr set difference": ["setdiff()", Key("left")],
    "deplyr semi join": ["semi_join()", Key("left")],
    "deplyr anti join": ["anti_join()", Key("left")],

    "reader right": ["write_"],
    "reader read": ["read_"],

    "deplyr schema": ['tbl(con, in_schema("public", "f_ttd_performance"))']
}

ctx.keymap(keymap)

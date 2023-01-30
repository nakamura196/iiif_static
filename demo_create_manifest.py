import json
import glob
import os

ID = "test"
LABEL = "テスト"
VHINT = "right-to-left"
DOCS_DIR = "docs"
GITHUB_URL = "https://nakamura196.github.io/iiif_static"

files = glob.glob(f"{DOCS_DIR}/files/tile/**/info.json", recursive=True)

files = sorted(files)

canvases = []

for i, file in enumerate(files):

    file = files[i]

    index = i + 1

    with open(file, encoding="utf8") as f:
        df = json.load(f)

        th_width = df["sizes"][0]["width"]
        th_height = df["sizes"][0]["height"]

        image_id = df["@id"]

        canvas = {
            "label": f"[{index}]",
            "width": df["width"],
            "height": df["height"],
            "@type": "sc:Canvas",
            "@id": f"{GITHUB_URL}/iiif/{ID}/canvas/p{index}",
            "images": [
                {
                    "@type": "oa:Annotation",
                    "on": f"{GITHUB_URL}/iiif/{ID}/canvas/p{index}",
                    "motivation": "sc:painting",
                    "resource": {
                        "@type": "dctypes:Image",
                        "format": "image/jpeg",
                        "width": df["width"],
                        "height": df["height"],
                        "@id": image_id + "/full/full/0/default.jpg",
                        "service": {
                          "@context": "http://iiif.io/api/image/2/context.json",
                          "@id": image_id,
                          "profile": "http://iiif.io/api/image/2/level0.json"
                        }
                    }
                }
            ],
            "thumbnail": {
                "@id": image_id + f"/full/{th_width},/0/default.jpg",
                "@type": "dctypes:Image",
                "format": "image/jpeg",
                "width": th_width,
                "height": th_height
            }
        }

        canvases.append(canvas)

manifest = {
    "label": LABEL,
    "@id": f"{GITHUB_URL}/iiif/{ID}/manifest.json",
    "@type": "sc:Manifest",
    "@context": "http://iiif.io/api/presentation/2/context.json",
    "metadata": [],
    "within": "",
    "logo": "",
    "description": "",
    "viewingHint": "",
    "viewingDirection": VHINT,
    "license": "http://creativecommons.org/licenses/by/4.0/",
    "sequences": [
        {
            "@type": "sc:Sequence",
            "label": "Current Page Order",
            "@id": f"{GITHUB_URL}/iiif/{ID}/sequence/normal",
            "canvases": canvases
        }
    ]
}

path = f"{DOCS_DIR}/iiif/{ID}/manifest.json"

os.makedirs(os.path.dirname(path), exist_ok=True)

fw = open(path, 'w', encoding="utf8")
json.dump(manifest, fw, ensure_ascii=False, indent=4,
          sort_keys=True, separators=(',', ': '))
fw.close()

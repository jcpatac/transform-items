function transformItems(items) {
    /**
    * @name transformItems
    * @description structures a given array of objects into a directory-like format
    * @param {array} items
    *
    * @returns {array} structured array of objects
    */

    /**
        Group items with common parent into an array
        and put these groupings into a dictionary with the
        parent id as key
    */
    let parentIdGrouping = items.reduce((result, curr) => {
        (result[curr.parent || 0] = result[curr.parent || 0] || []).push(curr);
        return result;
    }, {});

	let getItemList = (depth, parentId, parentIdGrouping) => {
        /**
        * @name getItemList
        * @description groups the items into their respective parent nodes
        * @param {int} depth
        * @param {int} parentId
        * @param {object} parentIdGrouping
        *
        * @returns {array} grouped items
        */

        // Sort siblings
		let currList = parentIdGrouping[parentId].sort((x, y) => {
			return x.seqId - y.seqId;
		});

		let itemList = [];

		currList.forEach(item => {
			item['depth'] = depth;
			itemList.push(item);

			if (parentIdGrouping[item.id]) {
				itemList = itemList.concat(getItemList(depth + 1, item.id, parentIdGrouping));
			}
		});
		return itemList;
	};
	return getItemList(0, 0, parentIdGrouping);
}


const items = [
	{ id: 2, seqId: 4, parent: 5, name: "index.tsx" },
	{ id: 3, seqId: 3, parent: 1, name: "Sidebar" },
	{ id: 4, seqId: 5, parent: 1, name: "Table" },
	{ id: 7, seqId: 5, parent: 5, name: "SelectableDropdown.tsx" },
	{ id: 5, seqId: 2, parent: 1, name: "AssignmentTable" },
	{ id: 1, seqId: 1, parent: null, name: "components" },
	{ id: 6, seqId: 2, parent: null, name: "controllers" },
];

const finalItems = transformItems(items);
console.log(finalItems);

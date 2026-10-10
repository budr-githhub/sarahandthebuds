import {test} from 'node:test';
import assert from 'node:assert/strict';
import {validate,calendarDoc} from './calendar.mjs';
const venues={wildside:{name:'Wildside',city:'Versailles',url:'https://example.com'}};
const show={name:'Test',start:'2027-03-21',startTime:'14:00',endTime:'17:00',act:'full-band',venueId:'wildside',status:'published'};
test('valid show, blank optional end date, and overnight event',()=>{
 assert.deepEqual(validate([{...show,end:''}],venues),[]);
 assert.deepEqual(validate([{...show,startTime:'23:00',endTime:'01:00',end:'2027-03-22'}],venues),[]);
});
test('reject impossible dates, reversed times, missing custom act and unsafe links',()=>{
 for(const patch of [{start:'2027-02-30'},{endTime:'13:00'},{venueId:'missing'},{act:'other'},{url:'javascript:alert(1)'},{status:'unknown'}])assert.ok(validate([{...show,...patch}],venues).length);
});
test('draft can be incomplete and is excluded from generated inventory; cancellation stays',()=>{
 const rows=[{name:'Hidden draft',status:'draft'},{...show,status:'cancelled'}];
 assert.deepEqual(validate(rows,venues),[]);
 const doc=calendarDoc(rows,venues);assert.ok(!doc.includes('Hidden draft'));assert.ok(doc.includes('cancelled'));
});

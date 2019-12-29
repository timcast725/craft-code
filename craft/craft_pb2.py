# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: craft.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='craft.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0b\x63raft.proto\"0\n\x05\x45ntry\x12\x18\n\x05\x65ntry\x18\x01 \x01(\x0b\x32\t.LogEntry\x12\r\n\x05index\x18\x02 \x01(\x05\"Z\n\x08Proposal\x12\x18\n\x05\x65ntry\x18\x01 \x01(\x0b\x32\t.LogEntry\x12\r\n\x05index\x18\x02 \x01(\r\x12\x13\n\x0b\x63ommitIndex\x18\x03 \x01(\r\x12\x10\n\x08proposer\x18\x04 \x01(\t\"L\n\x08LogEntry\x12\x0c\n\x04term\x18\x01 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\t\x12\x12\n\nappendedBy\x18\x03 \x01(\x08\x12\x10\n\x08proposer\x18\x04 \x01(\t\"\x86\x01\n\x07\x45ntries\x12\x0c\n\x04term\x18\x01 \x01(\x05\x12\x10\n\x08leaderId\x18\x02 \x01(\t\x12\x14\n\x0cprevLogIndex\x18\x03 \x01(\x05\x12\x13\n\x0bprevLogTerm\x18\x04 \x01(\x05\x12\x1a\n\x07\x65ntries\x18\x05 \x03(\x0b\x32\t.LogEntry\x12\x14\n\x0cleaderCommit\x18\x06 \x01(\x05\"$\n\x03\x41\x63k\x12\x0c\n\x04term\x18\x01 \x01(\x05\x12\x0f\n\x07success\x18\x02 \x01(\x08\"[\n\x0bVoteRequest\x12\x0c\n\x04term\x18\x01 \x01(\x05\x12\x13\n\x0b\x63\x61ndidateId\x18\x02 \x01(\t\x12\x14\n\x0clastLogIndex\x18\x03 \x01(\x05\x12\x13\n\x0blastLogTerm\x18\x04 \x01(\x05\x32\x83\x02\n\x05\x63Raft\x12#\n\x0bRequestVote\x12\x0c.VoteRequest\x1a\x04.Ack\"\x00\x12!\n\rAppendEntries\x12\x08.Entries\x1a\x04.Ack\"\x00\x12\x1d\n\x0b\x41ppendEntry\x12\x06.Entry\x1a\x04.Ack\"\x00\x12\'\n\x13GlobalAppendEntries\x12\x08.Entries\x1a\x04.Ack\"\x00\x12#\n\x0eReceivePropose\x12\t.Proposal\x1a\x04.Ack\"\x00\x12)\n\x14GlobalReceivePropose\x12\t.Proposal\x1a\x04.Ack\"\x00\x12\x1a\n\x08Notified\x12\x06.Entry\x1a\x04.Ack\"\x00\x62\x06proto3')
)




_ENTRY = _descriptor.Descriptor(
  name='Entry',
  full_name='Entry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entry', full_name='Entry.entry', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='index', full_name='Entry.index', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=15,
  serialized_end=63,
)


_PROPOSAL = _descriptor.Descriptor(
  name='Proposal',
  full_name='Proposal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entry', full_name='Proposal.entry', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='index', full_name='Proposal.index', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='commitIndex', full_name='Proposal.commitIndex', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proposer', full_name='Proposal.proposer', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=65,
  serialized_end=155,
)


_LOGENTRY = _descriptor.Descriptor(
  name='LogEntry',
  full_name='LogEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='term', full_name='LogEntry.term', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='LogEntry.data', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='appendedBy', full_name='LogEntry.appendedBy', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proposer', full_name='LogEntry.proposer', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=157,
  serialized_end=233,
)


_ENTRIES = _descriptor.Descriptor(
  name='Entries',
  full_name='Entries',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='term', full_name='Entries.term', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='leaderId', full_name='Entries.leaderId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prevLogIndex', full_name='Entries.prevLogIndex', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prevLogTerm', full_name='Entries.prevLogTerm', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entries', full_name='Entries.entries', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='leaderCommit', full_name='Entries.leaderCommit', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=236,
  serialized_end=370,
)


_ACK = _descriptor.Descriptor(
  name='Ack',
  full_name='Ack',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='term', full_name='Ack.term', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='success', full_name='Ack.success', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=372,
  serialized_end=408,
)


_VOTEREQUEST = _descriptor.Descriptor(
  name='VoteRequest',
  full_name='VoteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='term', full_name='VoteRequest.term', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='candidateId', full_name='VoteRequest.candidateId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lastLogIndex', full_name='VoteRequest.lastLogIndex', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lastLogTerm', full_name='VoteRequest.lastLogTerm', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=410,
  serialized_end=501,
)

_ENTRY.fields_by_name['entry'].message_type = _LOGENTRY
_PROPOSAL.fields_by_name['entry'].message_type = _LOGENTRY
_ENTRIES.fields_by_name['entries'].message_type = _LOGENTRY
DESCRIPTOR.message_types_by_name['Entry'] = _ENTRY
DESCRIPTOR.message_types_by_name['Proposal'] = _PROPOSAL
DESCRIPTOR.message_types_by_name['LogEntry'] = _LOGENTRY
DESCRIPTOR.message_types_by_name['Entries'] = _ENTRIES
DESCRIPTOR.message_types_by_name['Ack'] = _ACK
DESCRIPTOR.message_types_by_name['VoteRequest'] = _VOTEREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Entry = _reflection.GeneratedProtocolMessageType('Entry', (_message.Message,), {
  'DESCRIPTOR' : _ENTRY,
  '__module__' : 'craft_pb2'
  # @@protoc_insertion_point(class_scope:Entry)
  })
_sym_db.RegisterMessage(Entry)

Proposal = _reflection.GeneratedProtocolMessageType('Proposal', (_message.Message,), {
  'DESCRIPTOR' : _PROPOSAL,
  '__module__' : 'craft_pb2'
  # @@protoc_insertion_point(class_scope:Proposal)
  })
_sym_db.RegisterMessage(Proposal)

LogEntry = _reflection.GeneratedProtocolMessageType('LogEntry', (_message.Message,), {
  'DESCRIPTOR' : _LOGENTRY,
  '__module__' : 'craft_pb2'
  # @@protoc_insertion_point(class_scope:LogEntry)
  })
_sym_db.RegisterMessage(LogEntry)

Entries = _reflection.GeneratedProtocolMessageType('Entries', (_message.Message,), {
  'DESCRIPTOR' : _ENTRIES,
  '__module__' : 'craft_pb2'
  # @@protoc_insertion_point(class_scope:Entries)
  })
_sym_db.RegisterMessage(Entries)

Ack = _reflection.GeneratedProtocolMessageType('Ack', (_message.Message,), {
  'DESCRIPTOR' : _ACK,
  '__module__' : 'craft_pb2'
  # @@protoc_insertion_point(class_scope:Ack)
  })
_sym_db.RegisterMessage(Ack)

VoteRequest = _reflection.GeneratedProtocolMessageType('VoteRequest', (_message.Message,), {
  'DESCRIPTOR' : _VOTEREQUEST,
  '__module__' : 'craft_pb2'
  # @@protoc_insertion_point(class_scope:VoteRequest)
  })
_sym_db.RegisterMessage(VoteRequest)



_CRAFT = _descriptor.ServiceDescriptor(
  name='cRaft',
  full_name='cRaft',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=504,
  serialized_end=763,
  methods=[
  _descriptor.MethodDescriptor(
    name='RequestVote',
    full_name='cRaft.RequestVote',
    index=0,
    containing_service=None,
    input_type=_VOTEREQUEST,
    output_type=_ACK,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AppendEntries',
    full_name='cRaft.AppendEntries',
    index=1,
    containing_service=None,
    input_type=_ENTRIES,
    output_type=_ACK,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AppendEntry',
    full_name='cRaft.AppendEntry',
    index=2,
    containing_service=None,
    input_type=_ENTRY,
    output_type=_ACK,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GlobalAppendEntries',
    full_name='cRaft.GlobalAppendEntries',
    index=3,
    containing_service=None,
    input_type=_ENTRIES,
    output_type=_ACK,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ReceivePropose',
    full_name='cRaft.ReceivePropose',
    index=4,
    containing_service=None,
    input_type=_PROPOSAL,
    output_type=_ACK,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GlobalReceivePropose',
    full_name='cRaft.GlobalReceivePropose',
    index=5,
    containing_service=None,
    input_type=_PROPOSAL,
    output_type=_ACK,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Notified',
    full_name='cRaft.Notified',
    index=6,
    containing_service=None,
    input_type=_ENTRY,
    output_type=_ACK,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CRAFT)

DESCRIPTOR.services_by_name['cRaft'] = _CRAFT

# @@protoc_insertion_point(module_scope)

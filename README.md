# Nano RPC

A CLI wrapper for the Nano RPC API. All commands are parsed from the official documentation markdown.

## Usage

```
usage: nano_rpc [-r] [-u URL]
                {account_balance,account_block_count,account_get,account_history,account_info,account_key,account_representative,account_weight,accounts_balances,accounts_frontiers,accounts_pending,active_difficulty,available_supply,block_account,block_confirm,block_count,block_create,block_hash,block_info,blocks,blocks_info,bootstrap,bootstrap_any,bootstrap_lazy,bootstrap_status,chain,confirmation_active,confirmation_height_currently_processing,confirmation_history,confirmation_info,confirmation_quorum,database_txn_tracker,delegators,delegators_count,deterministic_key,epoch_upgrade,frontier_count,frontiers,keepalive,key_create,key_expand,ledger,node_id,node_id_delete,peers,pending,pending_exists,process,representatives,representatives_online,republish,sign,stats,stats_clear,stop,successors,telemetry,validate_account_number,version,unchecked_clear,unchecked_get,unchecked_keys,unopened,uptime,work_cancel,work_generate,work_peer_add,work_peers,work_peers_clear,work_validate,account_create,account_list,account_move,account_remove,account_representative_set,accounts_create,password_change,password_enter,password_valid,receive,receive_minimum,receive_minimum_set,search_pending,search_pending_all,send,wallet_add,wallet_add_watch,wallet_balances,wallet_change_seed,wallet_contains,wallet_create,wallet_destroy,wallet_export,wallet_frontiers,wallet_history,wallet_info,wallet_ledger,wallet_lock,wallet_locked,wallet_pending,wallet_representative,wallet_representative_set,wallet_republish,wallet_work_get,work_get,work_set,krai_from_raw,krai_to_raw,mrai_from_raw,mrai_to_raw,rai_from_raw,rai_to_raw,block_count_type,payment_begin,payment_end,payment_init,payment_wait}
```

## Example

```
>$ nano_rpc wallet_balances --wallet 000D1BAEC8EC208142C99059B393051BAC8380F9B5A2E6B2489A277D81789F3F
{
    "balances": {
        "nano_3e3j5tkog48pnny9dmfzj1r16pg8t1e76dz5tmac6iq689wyjfpi00000000": {
            "balance": "10000",
            "pending": "10000"
        }
    }
}
```
